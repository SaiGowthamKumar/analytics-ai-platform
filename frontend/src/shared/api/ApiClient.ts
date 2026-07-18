export type ApiRequest = Readonly<{ path: string; signal?: AbortSignal }>;
export type ApiClientOptions = Readonly<{
  baseUrl?: string;
  timeoutMs?: number;
  fetchImplementation?: typeof fetch;
}>;

export class ApiClient {
  private readonly baseUrl: string;
  private readonly fetchImplementation: typeof fetch;
  private readonly timeoutMs: number;

  public constructor(options: ApiClientOptions = {}) {
    this.baseUrl = options.baseUrl ?? import.meta.env.VITE_API_BASE_URL ?? "/api/v1";
    this.timeoutMs = options.timeoutMs ?? 10_000;
    this.fetchImplementation = options.fetchImplementation ?? fetch;
  }

  public async request<TResponse>(request: ApiRequest): Promise<TResponse> {
    const timeoutController = new AbortController();
    const timeout = window.setTimeout(() => timeoutController.abort(), this.timeoutMs);
    const signal = request.signal
      ? AbortSignal.any([request.signal, timeoutController.signal])
      : timeoutController.signal;

    try {
      const response = await this.fetchImplementation(this.baseUrl + request.path, {
        headers: { Accept: "application/json" },
        method: "GET",
        signal,
      });

      if (!response.ok) {
        throw new ApiClientError(response.status, "The API request failed.");
      }

      return (await response.json()) as TResponse;
    } finally {
      window.clearTimeout(timeout);
    }
  }
}

export class ApiClientError extends Error {
  public constructor(
    public readonly status: number,
    message: string,
  ) {
    super(message);
    this.name = "ApiClientError";
  }
}

