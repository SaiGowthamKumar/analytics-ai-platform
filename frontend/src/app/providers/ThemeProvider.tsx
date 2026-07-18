import type { ReactNode } from "react";

type ThemeProviderProperties = Readonly<{ children: ReactNode }>;

export function ThemeProvider({ children }: ThemeProviderProperties): React.JSX.Element {
  return <div data-theme="base">{children}</div>;
}
