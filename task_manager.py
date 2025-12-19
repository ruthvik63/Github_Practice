class Task:
    """Class to represent a single task."""
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.is_completed = False

    def mark_complete(self):
        self.is_completed = True
        print(f"Task '{self.title}' is now complete.")

class WorkTask(Task):
    """Inheritance example: A specific type of task."""
    def __init__(self, title, description, deadline):
        super().__init__(title, description)
        self.deadline = deadline

# Professional Tip: Always use this check to run your code
if __name__ == "__main__":
    my_task = WorkTask("Finish Git Guide", "Explain branches and push", "Friday")
    print(f"Goal: {my_task.title} by {my_task.deadline}")