import pytest
from datetime import date, timedelta
from pawpal_system import Task, Pet, Owner, Scheduler

def test_sorting_correctness():
    """Verify tasks are returned in chronological order."""
    # Arrange
    scheduler = Scheduler()
    task1 = Task(description="Evening Walk", duration_minutes=30, priority="High", time="06:00 PM")
    task2 = Task(description="Morning Feed", duration_minutes=5, priority="High", time="08:00 AM")
    task3 = Task(description="Midday Play", duration_minutes=15, priority="Low", time="12:00 PM")
    
    # Create the tuple format that get_all_tasks returns
    tasks = [("Buddy", task1), ("Buddy", task2), ("Buddy", task3)]
    
    # Act
    sorted_tasks = scheduler.sort_tasks_by_time(tasks)
    
    # Assert
    assert sorted_tasks[0][1].time == "08:00 AM"
    assert sorted_tasks[1][1].time == "12:00 PM"
    assert sorted_tasks[2][1].time == "06:00 PM"

def test_recurrence_logic():
    """Confirm that marking a daily task complete creates a new task for the following day."""
    # Arrange
    today = date.today()
    task = Task(description="Give Meds", duration_minutes=5, priority="High", time="09:00 AM", frequency="Daily", task_date=today)
    
    # Act
    next_task = task.mark_complete()
    
    # Assert
    assert task.is_complete is True
    assert next_task is not None
    assert next_task.description == "Give Meds"
    assert next_task.task_date == today + timedelta(days=1)

def test_conflict_detection():
    """Verify that the Scheduler flags duplicate times."""
    # Arrange
    scheduler = Scheduler()
    task1 = Task(description="Walk Buddy", duration_minutes=30, priority="High", time="08:00 AM")
    task2 = Task(description="Feed Luna", duration_minutes=5, priority="Medium", time="08:00 AM")
    
    tasks = [("Buddy", task1), ("Luna", task2)]
    
    # Act
    warnings = scheduler.check_conflicts(tasks)
    
    # Assert
    assert len(warnings) == 1
    assert "CONFLICT" in warnings[0]
    assert "08:00 AM" in warnings[0]