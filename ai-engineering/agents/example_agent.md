# Agents - example patterns

This document sketches a simple agent pattern for automating a small workflow:

- Use a planner to break a user request into steps.
- Use specialized tools for each step (e.g., SQL executor, web search, code runner).
- Keep tool outputs small and validate before proceeding to the next step.

See ai-engineering/llm/quickstart.md for LLM-related tooling tips.
