tasks = [
    "Load PDF",
    "Extract Text",
    "Generate Summary",
    "Store Report"
]

print("\nStarting Automation...\n")

for step, task in enumerate(tasks, start=1):

    print(f"STEP {step}: {task}")

print("\nAutomation Completed!")