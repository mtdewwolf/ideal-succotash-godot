---
name: godot-threading-concurrency
description: Use for Godot 4 concurrency—WorkerThreadPool, callables, mutexes, and thread-safe APIs. Use when moving work off the main thread or fixing races; not a substitute for reading official thread-safety rules before touching RenderingServer or the scene tree from threads.
---

# Godot 4 — threading and concurrency

Use with **`godot-files-data-io`** for background loading patterns; with **`godot-http-websocket-tls`** for async network; with **`godot-4-engine-core`** for deferred scene-tree updates.

## When to use this skill

- **`WorkerThreadPool`**: short tasks with `submit` / `wait_for_task_to_finish` patterns appropriate to the engine version; avoid blocking the main thread waiting on long tasks every frame.
- **`Thread`**: long-running worker loops—clear shutdown signaling; never touch **most `Node` APIs** from a secondary thread.
- **Synchronization**: `Mutex`, `Semaphore`, or message passing with **thread-safe queues**—prefer copying plain data into the main thread via `call_deferred` or signals over sharing live node references.
- **Godot APIs that are thread-safe** (subset): follow the official list—**do not assume** a random `Object` method is safe off-thread.

## Principles

- Default stance: **main thread owns the scene tree**; worker threads produce **data** (meshes, AI search results, parsed files) that the main thread applies in `_process` or deferred calls.
- Use **`await`** and signals for concurrency without threads when that suffices.
- For **RenderingServer** or **servers** in general, read the **thread model** for your exact minor version before “optimizing” with threads.

## Pitfalls

- Calling **`get_node`**, **`add_child`**, or tweaking transforms from a **`Thread`** → undefined behavior / crashes.
- **Deadlocks**: main thread waits on worker while worker waits on main-thread-only API.

## Official reference

- Thread-safe APIs: https://docs.godotengine.org/en/stable/tutorials/performance/thread_safe_apis.html
- WorkerThreadPool: https://docs.godotengine.org/en/stable/classes/class_workerthreadpool.html
