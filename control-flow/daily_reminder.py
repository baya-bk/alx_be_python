# daily_reminder.py

# Ask the user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use match-case to handle task priority and if-statement for time sensitivity
match priority:
    case "high":
        message = f"'{task}' is a high priority task"
        if time_bound == "yes":
            message += " that requires immediate attention today!"
    case "medium":
        message = f"'{task}' is a medium priority task"
        if time_bound == "yes":
            message += " that you should aim to complete today."
    case "low":
        message = f"'{task}' is a low priority task"
        if time_bound == "yes":
            message += " that can be done when convenient today."

# For non-time-sensitive tasks, add this outside the match block
if time_bound == "no":
    message += ". Consider completing it when you have free time."

# Print the customized reminder
print(message)
