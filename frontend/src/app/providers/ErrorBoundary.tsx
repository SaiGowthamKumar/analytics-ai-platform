import { Component, type ErrorInfo, type ReactNode } from "react";

type ErrorBoundaryProperties = Readonly<{ children: ReactNode }>;
type ErrorBoundaryState = Readonly<{ has_error: boolean }>;

export class ErrorBoundary extends Component<ErrorBoundaryProperties, ErrorBoundaryState> {
  public state: ErrorBoundaryState = { has_error: false };

  public static getDerivedStateFromError(): ErrorBoundaryState {
    return { has_error: true };
  }

  public componentDidCatch(_error: Error, _errorInfo: ErrorInfo): void {
    // Telemetry is intentionally outside the bootstrap scope.
  }

  public render(): ReactNode {
    if (this.state.has_error) {
      return (
        <main className="error-fallback" role="alert">
          <h1>Something went wrong</h1>
          <p>Please refresh the page and try again.</p>
        </main>
      );
    }

    return this.props.children;
  }
}

