# daily_reminder.py

# Ask the user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use match-case to handle task priority and if-statement for time sensitivity
match priority:
    case "high":
        print(f"Reminder: '{task}' is a high priority task", end="")
        if time_bound == "yes":
            print(" that requires immediate attention today!")
        else:
            print(".")
    case "medium":
        print(f"Reminder: '{task}' is a medium priority task", end="")
        if time_bound == "yes":
            print(" that you should aim to complete today.")
        else:
            print(".")
    case "low":
        print(f"Note: '{task}' is a low priority task", end="")
        if time_bound == "yes":
            print(" that can be done when convenient today.")
        else:
            print(". Consider completing it when you have free time.")
