import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    coverage: {
      enabled: true,
      provider: "v8",
      reporter: ["text", "cobertura"],
    },
    environment: "jsdom",
    include: ["src/**/*.test.ts"],
  },
});
