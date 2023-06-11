import { Headers } from "../Headers/headers";
import { Outlet } from "react-router-dom";

export const BasicLayout = () => {
  return (
    <>
      <Headers />
      <Outlet />
    </>
  );
};
