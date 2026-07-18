import { Outlet } from "react-router-dom";

export function RootLayout(): React.JSX.Element {
  return (
    <div className="application-shell">
      <header className="application-header">Application</header>
      <div className="application-body">
        <aside className="application-sidebar" aria-label="Reserved navigation area" />
        <main className="application-main">
          <Outlet />
        </main>
      </div>
      <footer className="application-footer">Platform foundation</footer>
    </div>
  );
}
