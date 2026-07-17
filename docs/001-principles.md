# Neuron Engineering Principles

These principles define how Neuron is designed, built, and maintained.

They are long-term commitments and should only change with strong justification.

---

# 1. Async First

Every public API is asynchronous.

Neuron is built for modern I/O-heavy AI workloads.

Blocking operations are isolated behind adapters.

---

# 2. Provider Agnostic

Neuron never exposes provider-specific APIs.

Applications should work with OpenAI, Anthropic, Gemini, Ollama, vLLM, or future providers without changing business logic.

---

# 3. Strong Typing

Every public API must be fully type hinted.

Type safety is part of the developer experience.

---

# 4. Clean Architecture

Business logic must never depend on infrastructure.

Core modules define interfaces.

Providers implement those interfaces.

Dependencies always point inward.

---

# 5. Plugin Based

Every major capability is replaceable.

Examples:

- Models
- Memory
- Knowledge
- Tools
- Storage
- Authentication
- Observability

The core framework should never depend on concrete implementations.

---

# 6. Convention over Configuration

Developers should write Python.

Avoid unnecessary YAML, JSON, or XML configuration.

Sensible defaults are preferred.

---

# 7. Composition over Inheritance

Prefer composing small components over deep inheritance hierarchies.

---

# 8. Batteries Included

Neuron should provide a complete development experience.

Common capabilities should work together naturally.

---

# 9. Stable Public APIs

Breaking changes are avoided whenever possible.

Backward compatibility is a feature.

---

# 10. Developer Experience First

Simple APIs are more valuable than clever APIs.

If a feature is difficult to understand, redesign it.

Neuron should feel obvious.