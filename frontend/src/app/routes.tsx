import { Route, Routes } from "react-router-dom";

import { RootLayout } from "../shared/layout/RootLayout";
import { HomePlaceholder } from "./HomePlaceholder";
import { NotFoundPlaceholder } from "./NotFoundPlaceholder";

export function AppRoutes(): React.JSX.Element {
  return (
    <Routes>
      <Route element={<RootLayout />}>
        <Route index element={<HomePlaceholder />} />
        <Route path="*" element={<NotFoundPlaceholder />} />
      </Route>
    </Routes>
  );
}
