from pawpal_system import Owner, Pet, Task, Scheduler

def main():
    # 1. Create an Owner
    owner = Owner(name="Alonso")

    # 2. Create at least two Pets
    pet1 = Pet(name="Buddy", species="Dog")
    pet2 = Pet(name="Luna", species="Cat")
    owner.add_pet(pet1)
    owner.add_pet(pet2)

    # 3. Add at least three Tasks with different times
    task1 = Task(description="Morning Walk", duration_minutes=30, priority="High", time="07:30 AM", frequency="Daily")
    task2 = Task(description="Feed Breakfast", duration_minutes=5, priority="High", time="08:00 AM", frequency="Daily")
    task3 = Task(description="Play with Laser Pointer", duration_minutes=15, priority="Medium", time="06:00 PM")

    pet1.add_task(task1)
    pet1.add_task(task2)
    pet2.add_task(task3)

    # Mark a task complete just to see the status update
    task1.mark_complete()

    # 4. Print "Today's Schedule" to the terminal
    scheduler = Scheduler()
    schedule_output = scheduler.get_daily_plan(owner)
    
    print(schedule_output)

if __name__ == "__main__":
    main()