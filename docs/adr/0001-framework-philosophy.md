# ADR-0001

# Title

Neuron is an AI Application Framework

---

## Status

Accepted

---

## Context

Modern AI applications require developers to integrate many independent technologies including language models, vector databases, memory systems, orchestration frameworks, authentication, deployment, and observability.

Existing libraries solve individual problems but do not provide a unified application framework.

---

## Decision

Neuron will be designed as an AI Application Framework.

Neuron will not become:

- an LLM wrapper
- an Agent library
- a Prompt library
- a RAG framework
- a FastAPI replacement

Instead, Neuron provides a complete application architecture for AI systems.

---

## Consequences

The framework will focus on architecture rather than providers.

Every provider-specific implementation will exist behind interfaces.

Business logic should never depend on AI vendors.

Applications should remain portable across providers.
