---
name: godot-multiplayer-networking
description: Use for Godot 4 multiplayer—ENet, RPCs, multiplayer API, authority, spawning, sync, and common pitfalls. Use when adding or fixing netcode, lobby, or replicated game state.
---

# Godot 4 — multiplayer and networking

## When to use this skill

- **High-level multiplayer**: `MultiplayerAPI`, `multiplayer.is_server()`, `multiplayer.get_unique_id()`, **RPC** annotations (`@rpc`, `call_local`, `transfer_mode`), `rpc`, `rpc_id`.
- **Peers and hosting**: `ENetMultiplayerPeer`, dedicated server vs listen server, port binding, disconnect handling.
- **Spawning**: who may instantiate scenes, `MultiplayerSpawner` / authority patterns the project already uses—match existing replication style.
- **State sync**: what runs only on server vs all clients; avoiding double application of effects.

## Principles

- **Single authority** per gameplay object where possible (usually server for competitive; host or server depending on game type).
- Prefer **small, explicit RPCs** with clear names over giant “do everything” remote calls.
- Validate **client requests** on the authority before mutating shared state (anti-cheat and consistency).
- Use **`call_deferred`** when RPC or peer callbacks interact with the scene tree in ways that might race with disconnect or scene changes.

## Pitfalls

- Calling RPCs before the peer is connected or after disconnect—guard with `multiplayer.has_multiplayer_peer()` and peer validity checks.
- Assuming **`is_multiplayer_authority()`** without aligning with how nodes are spawned and which peer owns them—trace ownership in the project.

## Official reference

- High-level multiplayer: https://docs.godotengine.org/en/stable/tutorials/networking/high_level_multiplayer.html
- WebSocket / ENet specifics: follow the engine docs section for the transport the project uses.
