// ts/App.tsx
// App.tsx
import { Routes, Route } from "react-router-dom";
import LogoPage from "./pages/LogoPage";
import TopPage from "./pages/TopPage";

function App() {
  return (
    <div className="app-container">
      <Routes>
        {/* 最初にアクセスした時（パスが "/"）は LogoPage を出す */}
        <Route path="/" element={<LogoPage />} />
        {/* パスが "/top" になったら TopPage を出す */}
        <Route path="/top" element={<TopPage />} />
      </Routes>
    </div>
  );
}

export default App;