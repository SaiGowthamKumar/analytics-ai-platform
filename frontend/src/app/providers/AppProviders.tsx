import type { ReactNode } from "react";

import { ErrorBoundary } from "./ErrorBoundary";
import { QueryProvider } from "./QueryProvider";
import { ThemeProvider } from "./ThemeProvider";

type AppProvidersProperties = Readonly<{ children: ReactNode }>;

export function AppProviders({ children }: AppProvidersProperties): React.JSX.Element {
  return (
    <ErrorBoundary>
      <ThemeProvider>
        <QueryProvider>{children}</QueryProvider>
      </ThemeProvider>
    </ErrorBoundary>
  );
}
