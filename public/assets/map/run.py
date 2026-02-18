import json
import struct
import random

# 入力ファイルパス
INPUT_FILE = './CountryData.geojson'
# 出力ファイルパス
OUTPUT_BIN = './map_data.bin'
OUTPUT_META = './map_meta.json'

def main():
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 国タグ(ADM0_A3)と数値IDの対応表を作成
    # setを使って重複を排除し、ソートしてリスト化
    countries = set()
    features = data.get('features', [])
    
    for feature in features:
        props = feature.get('properties', {})
        country_code = props.get('ADM0_A3') or 'UNK'
        countries.add(country_code)
    
    # IDマップ作成 (例: {'GER': 0, 'FRA': 1, ...})
    country_to_id = {code: i for i, code in enumerate(sorted(list(countries)), start=1)}
    country_to_id["Ocean"] = 0
    
    # 国ごとの色をランダム生成 (本来は固定定義ファイルから読むべき)
    country_colors = {}
    for code in countries:
        # ランダムなHexカラー
        country_colors[code] = "#{:06x}".format(random.randint(0, 0xFFFFFF))

    # バイナリデータの作成
    # フォーマット:
    # grid_x (unsigned short, 2bytes)
    # grid_y (unsigned short, 2bytes)
    # owner_id (unsigned char, 1byte) - 255ヶ国以下と仮定
    # occupy_id (unsigned char, 1byte)
    
    binary_data = bytearray()
    
    for feature in features:
        props = feature.get('properties', {})
        
        g_x = int(props.get('col_index', 0))
        g_y = int(props.get('row_index', 0))
        
        # 国コードをIDに変換
        owner_code = props.get('ADM0_A3', 'UNK')
        owner_id = country_to_id.get(owner_code, 0)
        
        # occupyがあればそれを使用、なければownerと同じ
        occupy_code = props.get('occupy', owner_code)
        # データにoccupyがない場合やnullの場合はownerを使う
        if occupy_code is None:
            occupy_code = owner_code
        occupy_id = country_to_id.get(occupy_code, 0)

        # struct.packでバイナリ化 ('H'='unsigned short', 'B'='unsigned char')
        # 2 + 2 + 1 + 1 = 6 bytes per point
        try:
            packed = struct.pack('<HHBB', g_x, g_y, owner_id, occupy_id)
            binary_data.extend(packed)
        except Exception as e:
            print(f"Error packing data: {props} - {e}")

    # バイナリ書き出し
    with open(OUTPUT_BIN, 'wb') as f:
        f.write(binary_data)

    # メタデータ書き出し (IDから国コード/色を引くために必要)
    meta_data = {
        "id_map": {v: k for k, v in country_to_id.items()}, # ID -> Code
        "colors": country_colors
    }
    
    with open(OUTPUT_META, 'w', encoding='utf-8') as f:
        json.dump(meta_data, f, indent=2)

    print(f"Conversion complete.")
    print(f"Points: {len(features)}")
    print(f"Binary size: {len(binary_data)} bytes")

if __name__ == "__main__":
    main()