# daily_reminder.py

# Ask the user for task details
task = input("Enter your task: ")

# Loop until a valid priority is entered
while True:
    priority = input("Priority (high/medium/low): ").lower()
    if priority in ['high', 'medium', 'low']:
        break
    else:
        print("Please enter a valid priority (high/medium/low).")

# Loop until a valid response is entered for time-bound
while True:
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    if time_bound in ['yes', 'no']:
        break
    else:
        print("Please enter 'yes' or 'no'.")

# Use a match-case statement to react based on priority
match priority:
    case "high":
        message = f"'{task}' is a high priority task"
    case "medium":
        message = f"'{task}' is a medium priority task"
    case "low":
        message = f"'{task}' is a low priority task"

# Check if the task is time-bound and modify the message
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    message += ". Consider completing it when you have free time."

# Print the reminder message
print(message)
