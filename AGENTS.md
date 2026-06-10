# AGENTS.md — Frontend (Python · Flet)

> Architecture: Hexagonal + Vertical Slice + Screaming Architecture
> Language: Python 3.12+
> Framework: Flet
> Goal: Strong typing, scalability, maintainability, testability, and AI-agent friendly code.

---

# Core Principles

* Business-first folder structure.
* Feature isolation.
* Dependency Injection.
* Composition Root.
* Async-first for IO.
* Passive UI.
* Strict typing.
* Result Pattern.
* Ports & Adapters.

---

# Technology Standards

## Interfaces

Use:

```python
from typing import Protocol
```

Never use:

```python
ABC
abstractmethod
```

---

## Models

Use:

```python
from pydantic import BaseModel
```

For:

* Entities
* Domain Models
* DTOs
* Requests
* Responses
* Settings

Forbidden:

```python
dataclass
TypedDict
NamedTuple
```

---

## Classes

Use normal classes for:

* Services
* Adapters
* Containers
* State
* Factories
* Event Bus

---

## Generics

Use:

```python
TypeVar
Generic
```

Never use:

```python
Any
```

as a generic fallback.

---

## Typing

Mandatory:

```python
User | None
list[User]
dict[str, User]
```

Forbidden:

```python
Optional[User]
List[User]
Dict[str, User]
Any
type: ignore
cast()
```

All public APIs must be typed.

---

# Architecture Rules

## Dependency Direction

```text
UI
 ↓
Application
 ↓
Domain (Protocols)
 ↓
Adapters
 ↓
Infrastructure
```

Dependencies always point inward.

---

## Feature Isolation

Features may depend on:

```text
shared/
domain/
dto/
protocols/
```

Features must never import:

```text
adapters/
httpx
aiohttp
sqlite
redis
boto3
supabase
firebase
```

---

## Composition Root

Only:

```text
src/composition_root.py
```

may instantiate concrete classes.

Forbidden elsewhere:

```python
HttpApiClient()
AuthAdapter()
Repository()
```

---

# Project Structure

```text
src/
├── main.py
├── composition_root.py
│
├── features/
│   └── <domain>/
│       └── <feature>/
│           ├── domain/
│           │   ├── models.py
│           │   ├── interfaces.py
│           │   ├── enums.py
│           │   └── exceptions.py
│           │
│           ├── application/
│           │   └── service.py
│           │
│           ├── dto/
│           │   ├── request.py
│           │   └── response.py
│           │
│           └── ui/
│               ├── page.py
│               └── widgets/
│
├── adapters/
│   ├── api/
│   ├── websocket/
│   ├── storage/
│   └── auth/
│
├── shared/
│   ├── config.py
│   ├── kernel/
│   ├── state/
│   ├── contracts/
│   ├── types/
│   └── utils/
│
├── theme.py
└── assets/
```

---

# Layer Responsibilities

## Domain

Contains:

* Models
* Protocols
* Enums
* Domain Exceptions

Contains no infrastructure.

---

## Application

Contains:

* Use Cases
* Services
* Orchestration

Depends only on Protocols.

---

## Adapters

Contains:

* HTTP
* WebSocket
* Storage
* External APIs

Implements Protocols.

Contains no business logic.

---

## UI

Contains:

* Pages
* Widgets
* Rendering
* Event Handling

Contains no business logic.

---

# Request Flow

```text
Page
 → DTO
 → Service
 → Protocol
 → Adapter
 → Backend

Backend
 ← Adapter
 ← Result[T]
 ← Service
 ← Page
```

---

# Container Rules

Container must be a normal class.

Never:

```python
BaseModel
dataclass
```

Purpose:

* Dependency registration
* Dependency resolution

Nothing else.

---

# State Rules

State must be a normal class.

Never:

```python
BaseModel
dataclass
```

State may contain:

* Listeners
* Subscriptions
* Notifications
* Reactive updates

---

# Service Rules

Services:

* Depend on Protocols
* Return Result[T]
* Coordinate business flows

Services must not:

* Use HTTP directly
* Access storage directly
* Access Flet controls
* Return dictionaries

---

# Adapter Rules

Adapters:

* Implement Protocols
* Handle infrastructure concerns
* Map external data

Adapters must not:

* Contain business rules
* Contain UI logic

---

# Result Pattern

Expected failures:

```python
Result.fail(...)
```

Success:

```python
Result.ok(...)
```

Do not raise expected business errors.

---

# Routing Rules

All routes live in:

```text
shared/utils/router.py
```

Never hardcode route strings in pages.

Use centralized route constants.

---

# Configuration

Use:

```python
pydantic-settings
```

Environment variables must be strongly typed.

---

# Async Rules

Use async for:

* HTTP
* Database
* Storage
* Files
* WebSockets
* External APIs

Do not use async for pure computations.

---

# Testing Standards

```text
tests/
├── unit/
├── integration/
└── ui/
```

Unit Tests:

* Mock Protocols
* No network
* No database
* No Flet runtime

Integration Tests:

* Real adapters

UI Tests:

* Flet testing tools

Minimum coverage:

```text
80%
```

---

# Development Commands

```bash
flet run src/main.py

python src/main.py

ruff check src/
ruff format src/

mypy src/

pytest
```

---

# Quality Gates

Build fails if:

* Ruff fails
* Mypy fails
* Tests fail
* Any exists
* type: ignore exists

No exceptions.

---

# Agent Decision Rules

When creating:

| Create    | Use               |
| --------- | ----------------- |
| Interface | Protocol          |
| Entity    | BaseModel         |
| DTO       | BaseModel         |
| Request   | BaseModel         |
| Response  | BaseModel         |
| Service   | class             |
| Adapter   | class             |
| State     | class             |
| Container | class             |
| Generic   | TypeVar + Generic |

---

# Golden Rules

1. Protocol for interfaces.
2. Pydantic for models.
3. TypeVar + Generic for generics.
4. No Any.
5. No ABC.
6. No dataclass.
7. No type: ignore.
8. No business logic in UI.
9. Services depend only on Protocols.
10. Composition Root creates all dependencies.
11. Services return Result[T].
12. Async only for IO.
13. Feature isolation is mandatory.
14. Tests are mandatory.
15. Architecture must remain scalable and AI-agent friendly.

---

# Future Micro-Frontend Path

* Features can become standalone Flet applications.
* Shared contracts remain in shared/.
* Communication occurs through APIs or event bus.
* No direct feature-to-feature imports.
* Each module owns its dependencies.
