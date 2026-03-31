import streamlit as st

# Step 1: Import your backend logic!
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

# Step 2: Manage the Application "Memory"
# We store the Owner and Scheduler in session_state so they aren't erased when you click a button.
if "owner" not in st.session_state:
    st.session_state.owner = Owner(name="Jordan")
    # Add a default pet so the UI is ready to use immediately
    st.session_state.owner.add_pet(Pet(name="Mochi", species="dog"))

if "scheduler" not in st.session_state:
    st.session_state.scheduler = Scheduler()


st.title("🐾 PawPal+")

with st.expander("Scenario", expanded=False):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.
"""
    )

st.divider()

# --- PET MANAGEMENT ---
st.subheader("Pet Profile")
# Update the owner's name dynamically
owner_name = st.text_input("Owner name", value=st.session_state.owner.name)
st.session_state.owner.name = owner_name

col_p1, col_p2 = st.columns(2)
with col_p1:
    new_pet_name = st.text_input("Add a New Pet", value="Luna")
with col_p2:
    new_species = st.selectbox("Species", ["dog", "cat", "other"])

if st.button("Add Pet"):
    # Step 3a: Wiring UI to Logic (Creating a Pet)
    new_pet = Pet(name=new_pet_name, species=new_species)
    st.session_state.owner.add_pet(new_pet)
    st.success(f"Added {new_pet_name}!")

# Show current pets
if st.session_state.owner.pets:
    pet_names = [p.name for p in st.session_state.owner.pets]
    st.write(f"**Current Pets:** {', '.join(pet_names)}")


st.divider()

# --- TASK MANAGEMENT ---
st.markdown("### Add a Task")
st.caption("Schedule a care task. This feeds directly into your OOP Scheduler.")

if not st.session_state.owner.pets:
    st.info("No pets yet. Add one above to start scheduling tasks.")
else:
    col1, col2, col3 = st.columns(3)
    with col1:
        task_title = st.text_input("Task title", value="Morning walk")
        # Select which pet gets the task
        target_pet_name = st.selectbox("Assign to", pet_names)
    with col2:
        duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
        task_time = st.time_input("Time")
    with col3:
        priority = st.selectbox("Priority", ["High", "Medium", "Low"], index=0)
        frequency = st.selectbox("Frequency", ["Once", "Daily", "Weekly"])

    if st.button("Add task"):
        # Find the actual Pet object the user selected
        target_pet = next(p for p in st.session_state.owner.pets if p.name == target_pet_name)
        
        # Step 3b: Wiring UI to Logic (Creating a Task)
        new_task = Task(
            description=task_title,
            duration_minutes=int(duration),
            priority=priority,
            time=task_time.strftime("%I:%M %p"), # Format time to match our Phase 2 string logic
            frequency=frequency
        )
        target_pet.add_task(new_task)
        st.success(f"Added '{task_title}' to {target_pet_name}'s schedule!")


st.divider()

# --- SCHEDULING ---
st.subheader("Build Schedule")
st.caption("Click below to run your backend algorithms and generate the daily plan.")

if st.button("Generate schedule"):
    all_tasks = st.session_state.scheduler.get_all_tasks(st.session_state.owner)
    
    if not all_tasks:
        st.info("No tasks scheduled for today. Add some above!")
    else:
        # 1. Detect and display conflicts using Streamlit warnings
        warnings = st.session_state.scheduler.check_conflicts(all_tasks)
        if warnings:
            for warning in warnings:
                st.warning(warning, icon="⚠️")
        else:
            st.success("Looking good! No scheduling conflicts detected.", icon="✅")
            
        # 2. Sort tasks chronologically
        sorted_tasks = st.session_state.scheduler.sort_tasks_by_time(all_tasks)
        
        # 3. Format the output into a clean list of dictionaries for st.table
        st.markdown("### 📅 Today's Schedule")
        schedule_data = []
        for pet_name, task in sorted_tasks:
            status = "✅ Done" if task.is_complete else "⏳ Pending"
            schedule_data.append({
                "Time": task.time,
                "Pet": pet_name,
                "Task": task.description,
                "Duration (min)": task.duration_minutes,
                "Priority": task.priority,
                "Status": status
            })
        
        # Render a professional data table!
        st.table(schedule_data)