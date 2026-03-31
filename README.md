# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🧠 Smarter Scheduling
PawPal+ features an intelligent algorithmic layer to optimize your day:
* **Chronological Sorting:** Automatically sorts tasks by "HH:MM AM/PM" format using Python `lambda` keys.
* **Conflict Warnings:** Detects and flags double-booked tasks scheduled at the exact same time.
* **Daily Recurrence:** Automatically generates tomorrow's task when a "Daily" or "Weekly" task is marked complete.

## 🧪 Testing PawPal+
To ensure the reliability of the scheduling algorithms, PawPal+ includes an automated test suite built with `pytest`. 

**To run the tests:**
```bash
python -m pytest

## ✨ Core Features
PawPal+ relies on an intelligent, object-oriented scheduling backbone:
* **Smart Time Sorting:** Automatically parses "HH:MM AM/PM" strings and sorts all tasks chronologically across all pets.
* **Conflict Detection:** Identifies double-bookings and alerts the user with dynamic UI warnings.
* **Recurring Tasks:** Marking a "Daily" or "Weekly" task as complete seamlessly generates the next occurrence using `datetime` timedelta math.
* **Persistent Memory:** Utilizes Streamlit's `session_state` to retain Owner, Pet, and Task objects cleanly between browser interactions.

## 📸 Demo
