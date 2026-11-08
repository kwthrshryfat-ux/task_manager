class Task:
    def __init__(self, title, done=False):
        self.title = title
        self.done = done
    def mark_done(self):
        self.done = True

    def to_dict(self):
        return {"title": self.title, "done": self.done}

    @staticmethod
    def from_dict(data):
        return Task(data["title"], data["done"])

    def __str__(self):
        mark = "✓" if self.done else "✕"
        return f"[{mark}] {self.title}"

class Taskmanager:
    def __init__(self, tasks=None):
        self.tasks = tasks or [] 

    def add(self, title):
        self.tasks.append(Task(title))
        
    def remove(self, index):
        if not 0 <= index < len(self.tasks):
            raise IndexError("شماره وظیفه نامعتبر است")
        self.tasks.pop(index)

    def edit(self, index, new_title):
        if not 0 <= index < len(self.tasks):
            raise IndexError("شماره وظیفه نامعتبر است")
        self.tasks[index].title = new_title

    def complete(self, index):
        if not 0 <= index < len(self.tasks):
            raise IndexError("شماره وظیفه نامعتبر است")
        self.tasks[index].mark_done()

    def show(self):
        if not self.tasks:
            print("هیچ وظیفه ای ثبت نشده.")
        for i, t in enumerate(self.tasks, 1):
            print(f"{i}. {t}")
            
                    