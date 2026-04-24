---
name: godot-http-websocket-tls
description: Use for Godot 4 HTTPRequest, TLS/SSL options, REST-style APIs, and WebSocketPeer clients/servers. Use when integrating web services or raw sockets—not for high-level ENet multiplayer RPCs unless bridging protocols.
---

# Godot 4 — HTTP, WebSocket, and TLS

Use with **`godot-multiplayer-networking`** when the game uses Godot’s multiplayer API instead; use **`godot-files-data-io`** for local persistence of tokens or cache files.

## When to use this skill

- **`HTTPRequest`**: `request()`, headers, body encoding, reading `body.get_string_from_utf8()`, handling **redirects** and **timeouts**.
- **TLS**: `TLSOptions` for custom CA or client certs when the project talks to private APIs—never disable certificate verification in production code unless the user explicitly requests a dev-only hack and understands risk.
- **`WebSocketPeer`**: poll mode, `PACKET_PEER_STREAM`, connecting vs listening, framing text vs binary, backpressure basics.
- **Threading**: network callbacks often arrive on the main thread via signals—keep heavy parsing off the frame if profiling shows spikes.

## Principles

- **Separate** transport (HTTP/WS) from **game protocol** (JSON schema, versioning, auth headers).
- Store **secrets** (API keys) via environment, OS keystore, or server-side proxies—not committed plaintext in the repo.
- Use **structured errors**: map HTTP status and WebSocket close codes to user-visible messages where appropriate.

## Pitfalls

- Assuming **`request_completed`** always means success—check result code and HTTP status.
- Mixing **blocking** patterns on the main thread (busy loops waiting for network)—use signals/`await` compatible with the project’s style.

## Official reference

- HTTP client class: https://docs.godotengine.org/en/stable/classes/class_httprequest.html
- WebSocket: https://docs.godotengine.org/en/stable/classes/class_websocketpeer.html
