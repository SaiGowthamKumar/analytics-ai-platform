export function NotFoundPlaceholder(): React.JSX.Element {
  return (
    <section aria-labelledby="not-found-heading">
      <h1 id="not-found-heading">Page not found</h1>
      <p>The requested route is not available.</p>
    </section>
  );
}
