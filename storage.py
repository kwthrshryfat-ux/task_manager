import json
import os
from models import Task

FILE = "task.json"


def load_tasks():
    if not os.path.exists(FILE):
        return []
    try:
        with open(FILE, encoding="utf-8") as f:
            return [Task.from_dict(d) for d in json.load(f)]
    except (json.JSONDecodeError, KeyError):
        print("فایل tasks.json خراب است، با لیست خالی شروع می‌کنیم.")
        return []


def save_tasks(tasks):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump([t.to_dict() for t in tasks], f, ensure_ascii=False, indent=2)
           