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

My scheduler primarily considers time and scheduling conflicts (exact double-bookings). While tasks hold a priority attribute, I decided that chronological time was the most important constraint to build the daily plan around. A pet owner needs to see their day flowing sequentially from morning to night. I also prioritized basic conflict detection to ensure the owner doesn't accidentally schedule a dog walk and a cat feeding at the exact same minute.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

For conflict detection, I implemented an exact-match time check rather than calculating overlapping durations. While checking for overlapping durations (e.g., a 30-min task at 8:00 overlapping with a 5-min task at 8:15) is more realistic, simply checking for duplicate start times is significantly lighter on performance and easier to read. For a basic pet app, alerting the user to exact double-bookings is a sufficient "lightweight" warning.
---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

I used AI primarily as a coding assistant to scaffold boilerplate code from my UML design, write Pytest assertions, and figure out Streamlit's session_state quirks. The most helpful prompts were highly specific and constrained. Instead of asking "build me a scheduler," asking targeted questions like, "How do I sort a list of objects based on a string attribute formatted as '08:00 AM' using Python's datetime module?" yielded much better, plug-and-play results.

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

When building the conflict detection logic, the AI suggested a complex algorithm using datetime timedeltas to check for overlapping intervals based on the duration_minutes of each task. I evaluated this and realized it was over-engineered for the current scope. I rejected it and instead implemented a simpler exact-match dictionary check that just looks for duplicate start times. This kept the code readable and lightweight while still fulfilling the core requirement.

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

I tested three core behaviors using Pytest: chronological sorting, conflict detection (flagging duplicate times), and recurrence logic (ensuring a completed "Daily" task spawns a new task for tomorrow). These tests were crucial because they represent the "brain" of the application. If sorting fails, the schedule is unreadable; if recurrence fails, the user loses their data.

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

I am very confident in the "happy path" of the scheduler based on the automated tests. However, if I had more time, I would test edge cases like tasks spanning across midnight, what happens if a user inputs an invalid time format, and true overlapping durations (e.g., a 60-minute walk starting at 8:00 AM conflicting with a 10-minute feeding at 8:30 AM).

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

I am most satisfied with successfully connecting the backend Object-Oriented logic to the Streamlit UI. Seeing the raw Python terminal output transform into a clean, interactive web table with functional buttons was incredibly rewarding.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

In another iteration, I would implement real data persistence. Right now, everything lives in Streamlit's session_state, meaning if the browser refreshes, the data is lost. I would redesign the backend to save and load Owner and Task data from a JSON file or a lightweight SQLite database.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?

I learned that AI is a fantastic coder but a poor architect without human guidance. You cannot rely on AI to design the system for you; you have to define the classes, the relationships (UML), and the data flow first. Once you act as the "lead architect" and set the boundaries, the AI becomes an incredibly powerful tool to fill in the syntax quickly.
