import type { ReactNode } from "react";

type QueryProviderProperties = Readonly<{ children: ReactNode }>;

export function QueryProvider({ children }: QueryProviderProperties): React.JSX.Element {
  return <>{children}</>;
}

