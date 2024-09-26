# daily_reminder.py

def get_task_details():
    # Prompt for task details
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    return task, priority, time_bound


def build_reminder(task, priority, time_bound):
    match priority:
        case "high":
            message = f"'{task}' is a high priority task"
        case "medium":
            message = f"'{task}' is a medium priority task"
        case "low":
            message = f"'{task}' is a low priority task"
        case _:
            message = f"'{task}' has an undefined priority"

    if time_bound == "yes":
        message += " that requires immediate attention today!"
    else:
        message += ". Consider completing it when you have free time."

    return message


def main():
    # Get task details
    task, priority, time_bound = get_task_details()

    # Build and display the reminder
    reminder = build_reminder(task, priority, time_bound)
    print(reminder)


if __name__ == "__main__":
    main()
