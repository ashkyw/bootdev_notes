class TodoList:
    def __init__(self, name: str) -> None:
        self.name = name
        self.tasks = []

    def add_task(self, description: str) -> None:
        task = {
            "description": description,
            "done": False,
        }
        self.tasks.append(task)

    def complete_task(self, description: str) -> bool:
        for task in self.tasks:
            if task["description"] == description and task["done"] is False:
                task["done"] = True
                return True
        return False

    def get_pending_tasks(self) -> list:
        self.pending_list = self.create_list(False)
        return self.pending_list
    
    def get_completed_tasks(self) -> list:
        self.completed_list = self.create_list(True)
        return self.completed_list

    def get_summary(self) -> str:
        return f"Todo List '{self.name}': {len(self.pending_list)} pending, {len(self.completed_list)} completed"

    def create_list(self, done_value: bool) -> list:
        new_list = []
        
        for task in self.tasks:
            if task["done"] == done_value:
                new_list.append(task["description"])

        return new_list
