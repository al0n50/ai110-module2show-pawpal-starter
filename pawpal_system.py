from dataclasses import dataclass, field
from typing import List

@dataclass
class Task:
    """Represents a single care activity for a pet."""
    description: str
    duration_minutes: int
    priority: str      # e.g., "High", "Medium", "Low"
    time: str          # e.g., "08:00 AM"
    frequency: str = "Once"  # Added per Phase 2 instructions
    is_complete: bool = False

    def mark_complete(self) -> None:
        """Marks the task as completed."""
        self.is_complete = True


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
        all_tasks = []
        for pet in owner.pets:
            for task in pet.tasks:
                all_tasks.append((pet.name, task))
        return all_tasks

    def get_daily_plan(self, owner: Owner) -> str:
        """Generates a formatted, readable daily schedule for the terminal."""
        tasks = self.get_all_tasks(owner)
        if not tasks:
            return "No tasks scheduled for today."
        
        # Simple string-based time sort (you will upgrade this in Phase 4)
        tasks.sort(key=lambda x: x[1].time)

        plan = f"\n📅 Today's Schedule for {owner.name}'s Pets:\n"
        plan += "=" * 50 + "\n"
        for pet_name, task in tasks:
            status = "✅" if task.is_complete else "⏳"
            plan += f"[{task.time}] {pet_name}: {task.description} ({task.duration_minutes}m, Priority: {task.priority}) {status}\n"
        return plan