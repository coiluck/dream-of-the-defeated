// ts/App.tsx
// App.tsx
import { Routes, Route } from "react-router-dom";
import LogoPage from "./pages/LogoPage";
import TopPage from "./pages/TopPage";

function App() {
  return (
    <div className="app-container">
      <Routes>
        <Route path="/" element={<LogoPage />} />
        <Route path="/top" element={<TopPage />} />
      </Routes>
      {/* ボタン用のフィルター */}
      <svg style={{ width: 0, height: 0, position: 'absolute', pointerEvents: 'none' }}>
        <defs>
          <filter id="button-grunge-filter">
            <feTurbulence type="fractalNoise" baseFrequency="0.05" numOctaves="2" result="noise" />
            <feDisplacementMap in="SourceGraphic" in2="noise" scale="2" xChannelSelector="R" yChannelSelector="G" />
          </filter>
        </defs>
      </svg>
    </div>
  );
}

export default App;