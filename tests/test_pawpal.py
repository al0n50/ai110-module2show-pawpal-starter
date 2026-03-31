import pytest
from pawpal_system import Task, Pet

def test_task_completion():
    """Verify that calling mark_complete() actually changes the task's status."""
    # Arrange
    task = Task(description="Brush fur", duration_minutes=10, priority="Low", time="10:00 AM")
    
    # Assert Initial State
    assert task.is_complete is False
    
    # Act
    task.mark_complete()
    
    # Assert Final State
    assert task.is_complete is True

def test_task_addition():
    """Verify that adding a task to a Pet increases that pet's task count."""
    # Arrange
    pet = Pet(name="Max", species="Dog")
    task = Task(description="Give medication", duration_minutes=2, priority="High", time="09:00 AM")
    
    initial_count = len(pet.tasks)
    
    # Act
    pet.add_task(task)
    
    # Assert
    assert len(pet.tasks) == initial_count + 1
    assert pet.tasks[0] == task