from pawpal_system import Owner, Pet, Task, Scheduler

def main():
    owner = Owner(name="Alonso")
    pet1 = Pet(name="Buddy", species="Dog")
    pet2 = Pet(name="Luna", species="Cat")
    owner.add_pet(pet1)
    owner.add_pet(pet2)

    # Adding tasks out of order to test sorting, and at the same time to test conflicts
    task1 = Task(description="Evening Walk", duration_minutes=30, priority="High", time="06:00 PM")
    task2 = Task(description="Morning Feed", duration_minutes=5, priority="High", time="08:00 AM", frequency="Daily")
    task3 = Task(description="Brush Fur", duration_minutes=15, priority="Medium", time="08:00 AM") # Conflict!

    pet1.add_task(task1)
    pet1.add_task(task2)
    pet2.add_task(task3)

    # Test Recurrence logic
    new_recurring_task = task2.mark_complete()
    if new_recurring_task:
        pet1.add_task(new_recurring_task)
        print(f"\n🔄 Daily task completed. Next occurrence scheduled for: {new_recurring_task.task_date}")

    # Generate Schedule
    scheduler = Scheduler()
    print(scheduler.get_daily_plan(owner))

if __name__ == "__main__":
    main()