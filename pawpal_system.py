from dataclasses import dataclass, field
from typing import List

@dataclass
class Task:
    description: str
    duration_minutes: int
    priority: str  # e.g., "High", "Medium", "Low"
    time: str      # e.g., "08:00 AM"
    is_complete: bool = False

    def mark_complete(self) -> None:
        """Marks the task as completed."""
        pass

@dataclass
class Pet:
    name: str
    species: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Assigns a new task to the pet."""
        pass

@dataclass
class Owner:
    name: str
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        """Adds a new pet to the owner's profile."""
        pass

class Scheduler:
    """The algorithmic brain that handles sorting and conflict detection."""
    
    def sort_tasks(self, tasks: List[Task]) -> List[Task]:
        """Sorts tasks by time or priority."""
        pass

    def check_conflicts(self, tasks: List[Task]) -> List[str]:
        """Detects overlapping times or impossible schedules."""
        pass

    def get_daily_plan(self, owner: Owner) -> dict:
        """Retrieves all tasks for an owner's pets and generates a schedule."""
        pass