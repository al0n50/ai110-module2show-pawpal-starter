from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime, timedelta, date

@dataclass
class Task:
    """Represents a single care activity for a pet."""
    description: str
    duration_minutes: int
    priority: str      
    time: str          
    frequency: str = "Once"  
    is_complete: bool = False
    task_date: date = field(default_factory=date.today) # Added to track recurrences

    def mark_complete(self) -> Optional['Task']:
        """
        Marks the task as completed. 
        If it is a recurring task, it automatically generates and returns the next occurrence.
        """
        self.is_complete = True
        
        # Step 3: Automate Recurring Tasks
        if self.frequency == "Daily":
            return Task(
                description=self.description, duration_minutes=self.duration_minutes,
                priority=self.priority, time=self.time, frequency=self.frequency,
                task_date=self.task_date + timedelta(days=1)
            )
        elif self.frequency == "Weekly":
            return Task(
                description=self.description, duration_minutes=self.duration_minutes,
                priority=self.priority, time=self.time, frequency=self.frequency,
                task_date=self.task_date + timedelta(days=7)
            )
        return None


@dataclass
class Pet:
    """Stores pet details and a list of their tasks."""
    name: str
    species: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Assigns a new task to the pet."""
        self.tasks.append(task)


@dataclass
class Owner:
    """Manages multiple pets and provides access to all their tasks."""
    name: str
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        """Adds a new pet to the owner's profile."""
        self.pets.append(pet)


class Scheduler:
    """The algorithmic brain that retrieves, organizes, and manages tasks across pets."""

    def get_all_tasks(self, owner: Owner) -> List[tuple]:
        """Retrieves all tasks from the owner's pets, returned as (pet_name, task) tuples."""
        return [(pet.name, task) for pet in owner.pets for task in pet.tasks]

    def sort_tasks_by_time(self, tasks: List[tuple]) -> List[tuple]:
        """Sorts tasks chronologically using datetime parsing."""
        return sorted(tasks, key=lambda x: datetime.strptime(x[1].time, "%I:%M %p"))

    def filter_tasks(self, tasks: List[tuple], pet_name: str = None, status: bool = None) -> List[tuple]:
        """Filters a list of tasks by pet name and/or completion status."""
        filtered = tasks
        if pet_name:
            filtered = [t for t in filtered if t[0] == pet_name]
        if status is not None:
            filtered = [t for t in filtered if t[1].is_complete == status]
        return filtered

    def check_conflicts(self, tasks: List[tuple]) -> List[str]:
        """Detects if multiple tasks are scheduled at the exact same time."""
        seen_times = {}
        warnings = []
        for pet_name, task in tasks:
            if task.time in seen_times:
                warnings.append(f"⚠️ CONFLICT: {pet_name}'s '{task.description}' overlaps with {seen_times[task.time]} at {task.time}!")
            else:
                seen_times[task.time] = f"{pet_name}'s '{task.description}'"
        return warnings

    def get_daily_plan(self, owner: Owner) -> str:
        """Generates a formatted, readable daily schedule with conflict detection and sorting."""
        all_tasks = self.get_all_tasks(owner)
        if not all_tasks:
            return "No tasks scheduled for today."
        
        # Apply our new algorithms!
        warnings = self.check_conflicts(all_tasks)
        sorted_tasks = self.sort_tasks_by_time(all_tasks)

        plan = f"\n📅 Today's Schedule for {owner.name}'s Pets:\n"
        plan += "=" * 55 + "\n"
        
        if warnings:
            for warning in warnings:
                plan += f"{warning}\n"
            plan += "-" * 55 + "\n"

        for pet_name, task in sorted_tasks:
            status = "✅" if task.is_complete else "⏳"
            plan += f"[{task.time}] {pet_name}: {task.description} ({task.duration_minutes}m) {status}\n"
        return plan