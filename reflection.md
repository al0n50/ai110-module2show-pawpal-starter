# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

My initial design followed an object-oriented approach centered around four main classes to separate the data from the scheduling logic:

Task: Responsible for holding the details of a single care activity. It tracks attributes like description, duration_minutes, priority, time, and a boolean is_complete status.

Pet: Represents the animal receiving care. It stores basic info (name, species) and is responsible for maintaining a list of its assigned Task objects.

Owner: Acts as the top-level user entity. It stores the owner's name and maintains a list of Pet objects, representing a "has-a" composition relationship.

Scheduler: Functions as the algorithmic "brain" of the app. Instead of holding data, it is responsible for processing it—specifically pulling tasks from the owner's pets, sorting them by priority/time, and checking for schedule conflicts to generate a daily plan.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

Yes, the design required adjustments once I started implementing the Scheduler logic. Initially, I designed the Task class to store the time attribute as a simple string (e.g., "08:00 AM"). However, when implementing the check_conflicts and sort_tasks methods, I realized that calculating overlapping durations and sorting string-based times was highly inefficient and prone to bugs. I updated the Task class to utilize Python's built-in datetime.time objects instead of strings, and added an end_time property that calculates automatically based on the duration_minutes. This change allowed the Scheduler to use simple math (e.g., task1.end_time > task2.start_time) to detect conflicts accurately.
---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
