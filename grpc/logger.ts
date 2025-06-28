// Simple timestamped logger utility for the gRPC client & examples

export function log(...args: unknown[]): void {
  const timestamp = new Date().toISOString();
  // eslint-disable-next-line no-console
  console.log(`[${timestamp}]`, ...args);
} 