import "./App.css";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import { FE_PATHS } from "./constants/paths";
import { BasicLayout } from "./components/Layout/BasicLayout/basic-layout";
import { Homepage } from "./pages/Homepage/homepage";
import { useEffect } from "react";

function App() {
  useEffect(() => {
    async function fetchData() {}

    fetchData();
  }, []);

  return (
    <div>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<BasicLayout />}>
            <Route path={FE_PATHS.HOME} element={<Homepage />}></Route>
          </Route>
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
