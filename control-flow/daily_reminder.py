task = input("Enter your task: ")
task_priority = input("Priority(high/medium/low): ").lower()
time = input("Is it time bound? (yes/no): ").lower()

match task_priority:
    case "high":
        if time == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task}' is a high priority task. Consider completing it when you have a free time.")
    case "medium":
        if time == "yes":
            print(f"Reminder: '{task}' is a medium priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task}' is a medium priority task. Consider completing it when you have a free time.")
    case "low":
        if time == "yes":
            print(f"Reminder: '{task}' is a low priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task}' is a high priority task. Consider completing it when you have a free time.")