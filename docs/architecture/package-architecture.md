# Package Architecture

## Purpose

The package architecture defines how Neuron is organized. Each package has a single responsibility and clear boundaries. This makes the framework easier to understand, maintain, test, and extend.

---

# Package Structure

```text
src/
└── neuron/
    ├── __init__.py
    ├── app/
    ├── runtime/
    ├── core/
    ├── events/
    ├── plugins/
    ├── config/
    ├── dependency/
    ├── lifecycle/
    ├── agent/
    ├── model/
    ├── tool/
    ├── workflow/
    ├── memory/
    ├── knowledge/
    ├── server/
    ├── cli/
    └── utils/
```

---

# Package Responsibilities

## app

The entry point of every Neuron application.

Responsibilities:

* Create and manage `AIApp`
* Initialize the framework
* Coordinate application startup and shutdown

---

## runtime

The execution engine of Neuron.

Responsibilities:

* Execute asynchronous tasks
* Manage execution context
* Coordinate components
* Handle graceful shutdown

---

## core

The foundation of the framework.

Responsibilities:

* Base classes
* Interfaces
* Common types
* Shared exceptions
* Shared protocols

The `core` package should **not** contain application logic.

---

## events

Provides event-driven communication.

Responsibilities:

* Event definitions
* Event bus
* Event publishing
* Event subscriptions

---

## plugins

Supports framework extensibility.

Responsibilities:

* Discover plugins
* Load plugins
* Register plugins
* Manage plugin lifecycle

---

## config

Manages application configuration.

Responsibilities:

* Read configuration
* Validate configuration
* Provide configuration to the application

---

## dependency

Provides dependency injection.

Responsibilities:

* Register services
* Resolve dependencies
* Manage object lifetimes

---

## lifecycle

Controls the application lifecycle.

Responsibilities:

* Startup
* Shutdown
* Resource cleanup

---

## agent

Contains the Agent implementation.

Responsibilities:

* Agent execution
* Agent state
* Agent coordination

---

## model

Provides a provider-independent model interface.

Responsibilities:

* Define model contracts
* Connect to AI providers through adapters

The model package should never depend on a specific provider directly.

---

## tool

Represents executable tools.

Responsibilities:

* Tool definitions
* Tool execution
* Tool validation

---

## workflow

Manages multi-step execution.

Responsibilities:

* Workflow definitions
* Workflow execution
* Task coordination

---

## memory

Provides memory abstractions.

Responsibilities:

* Store state
* Retrieve state
* Memory interfaces

---

## knowledge

Provides knowledge abstractions.

Responsibilities:

* Access knowledge sources
* Document retrieval
* Knowledge interfaces

---

## server

Provides server integrations.

Responsibilities:

* HTTP APIs
* WebSocket support
* Request handling

---

## cli

Provides command-line functionality.

Responsibilities:

* Project creation
* Development commands
* Administrative commands

---

## utils

Contains small reusable helper functions.

Responsibilities:

* Utility functions
* Generic helpers

Utilities should remain small and should not contain business logic.

---

# Dependency Rules

Neuron follows a layered architecture.

```
AIApp
    │
    ▼
Runtime
    │
    ▼
Core Services
    │
    ▼
Application Components
    │
    ▼
Infrastructure
```

Dependencies always move **downward**.

Examples:

✅ Allowed

```
app → runtime
runtime → events
agent → core
workflow → core
server → app
```

❌ Not Allowed

```
core → app
core → runtime
events → app
model → runtime
```

Packages should never create circular dependencies.

---

# Core Package Rule

The `core` package is the foundation of Neuron.

It contains only shared abstractions such as:

* Base classes
* Interfaces
* Common types
* Exceptions
* Protocols

The `core` package must never contain:

* Business logic
* AI provider implementations
* HTTP server code
* Workflow logic
* Agent implementations

Every package may depend on `core`, but `core` should depend on no other Neuron package whenever possible.

---

# Design Principles

Every package in Neuron must follow these principles:

* One clear responsibility
* Clear boundaries
* Loose coupling
* High cohesion
* Async-first design
* Provider independence
* Strong typing
* Easy testing
* Easy extension

These principles help keep Neuron simple, maintainable, and scalable for many years.
