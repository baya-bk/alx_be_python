# daily_reminder.py

def get_task_details():
    # Prompt for task details
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    return task, priority, time_bound


def provide_reminder(task, priority, time_bound):
    match priority:
        case "high":
            reminder = f"'{task}' is a high priority task"
        case "medium":
            reminder = f"'{task}' is a medium priority task"
        case "low":
            reminder = f"'{task}' is a low priority task"
        case _:
            reminder = f"'{task}' has an undefined priority"

    # Add time-bound condition to the reminder
    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    else:
        reminder += ". Consider completing it when you have free time."

    print(f"\nReminder: {reminder}")


def main():
    # Get task details from the user
    task, priority, time_bound = get_task_details()

    # Provide customized reminder
    provide_reminder(task, priority, time_bound)


if __name__ == "__main__":
    main()
