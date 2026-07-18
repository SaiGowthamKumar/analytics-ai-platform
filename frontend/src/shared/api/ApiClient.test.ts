import { describe, expect, it } from "vitest";

import { ApiClient } from "./ApiClient";

describe("ApiClient", () => {
  it("uses the supplied base URL through its generic request abstraction", async () => {
    let requestedUrl = "";
    const client = new ApiClient({
      baseUrl: "https://example.test",
      fetchImplementation: async (input) => {
        requestedUrl = String(input);
        return new Response(JSON.stringify({ status: "ok" }), { status: 200 });
      },
    });

    await expect(client.request<{ status: string }>({ path: "/status" })).resolves.toEqual({
      status: "ok",
    });
    expect(requestedUrl).toBe("https://example.test/status");
  });
});
