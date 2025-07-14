
# 🤖 agents.md — AI Agent Instructions

This file defines the behavior, rules, and coding standards for any AI or automation tools contributing to this project.

## 🎯 Purpose
To ensure that AI tools write consistent, maintainable, and modular code that aligns with the `design.md`, `planning.md`, and `tickets.md`.

## 📘 Design Reference
- Always read `design.md` for overall goals and context
- Refer to `planning.md` for milestones and high-level tasks
- Create or update `tickets.md` for execution tasks

## 🔁 Task Behavior

- If no active ticket exists for the next milestone task, create one.
- If a ticket is too complex, break it down into sub-tickets (e.g. T3.2a, T3.2b).
- Always use the checklist format on tickets:
  - [ ] Started
  - [ ] Tests Written
  - [ ] Code Written
  - [ ] Tests Passed
  - [ ] Documentation Written
- Always verify in planning.md that which tasks are completed and mark them accordingly.
- Before creating the PR, always check planning.md and create new tickets for the next run.

## ✨ Coding Standards

### ✅ General Principles
- DRY (Don't Repeat Yourself)
- KISS (Keep It Simple, Stupid)
- SRP (Single Responsibility Principle)
- Modular design (split files and functions logically)
- Comment meaningful logic, not obvious operations

### 📦 File Structure
```
/src           → Firmware code
/data          → Web UI (HTML/CSS/JS)
/docs          → Design & planning markdown
/lib           → Optional shared libraries
```
