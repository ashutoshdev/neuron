# Core Concepts

Neuron is an AI-native application framework.

Every application built with Neuron is composed of a small set of fundamental concepts.

These concepts are intentionally few and stable.

---

# AIApp

The root object of every Neuron application.

Responsibilities:

- Lifecycle
- Configuration
- Plugin registration
- Dependency container
- Runtime startup

Every Neuron project starts here.

---

# Runtime

The execution engine.

Responsibilities:

- Execute tasks
- Manage async execution
- Maintain execution context
- Event dispatching
- Resource management

There is exactly one Runtime per AIApp.

---

# Agent

An autonomous execution unit.

Responsibilities:

- Understand tasks
- Use models
- Call tools
- Read knowledge
- Maintain memory

Agents never directly depend on providers.

---

# Model

Represents an AI model.

Examples:

- OpenAI
- Anthropic
- Gemini
- Ollama
- vLLM

Neuron communicates through the Model interface only.

---

# Tool

Represents an external capability.

Examples:

- HTTP
- SQL
- Weather
- Email
- GitHub
- Slack

Tools are asynchronous.

---

# Memory

Stores conversational or long-term state.

Memory implementations are replaceable.

---

# Knowledge

Represents information available to agents.

Knowledge may come from:

- Files
- PDFs
- Databases
- APIs
- Vector stores

The framework does not assume a storage mechanism.

---

# Workflow

Defines execution order.

Examples:

- Sequential
- Parallel
- Conditional
- Multi-agent

---

# Event

Represents something that happened inside the framework.

Examples:

- Agent started
- Tool executed
- Model completed
- Error occurred

Everything important should emit events.

---

# Plugin

Every extensible capability inside Neuron is implemented as a plugin.

Neuron Core depends on interfaces.

Plugins provide implementations.