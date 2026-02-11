// ts/pages/TopPage.tsx
import React from 'react';

import { useNavigate } from "react-router-dom"; // インポートするだけでOK

export default function TopPage() {
  const navigate = useNavigate(); // これさえあればどこへでも行ける

  return (
    <div style={{ textAlign: 'center', padding: '50px' }}>
      <h1>トップページ</h1>
      <p>ロゴアニメーションが終わってここにきました。</p>

      <div style={{ marginTop: '20px' }}>
        {/* ボタンを押したら「/」つまりロゴに戻る */}
        <button onClick={() => navigate('/')}>
          もう一度ロゴを見る
        </button>
      </div>
    </div>
  );
}