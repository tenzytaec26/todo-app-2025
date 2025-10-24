from dataclasses import dataclass, field
from datetime import datetime

ALLOWED_PRIORITIES = {"low", "medium", "high"}

class ToDo: 
  def __init__(self, id: int, title: str, done: bool = False, created_at: datetime | None = None, priority: str = "low"):
    self.id = id
    self.title = title
    self.done = done
    self.created_at = created_at or datetime.now()
    self.priority = priority


  def __repr__(self):
    return f"<ToDo {self.id}: {self.title} ({self.priority}, {'done' if self.done else 'pending'})>"


TASKS: list[ToDo] = []

def add_task(title: str, priority: str = "low") -> ToDo:
  new_id = TASKS[-1].id + 1 if TASKS else 1
  todo = ToDo(id=new_id, title=title, priority=priority)
  TASKS.append(todo)
  return todo

def get_tasks() -> list[ToDo]:
  return TASKS

def toggle_task(task_id: int) -> bool:
  for t in TASKS:
    if t.id == task_id:
      t.done = not t.done
      return True
  return False

def delete_task(task_id: int) -> None:
  global TASKS
  TASKS = [t for t in TASKS if t.id != task_id]

def get_tasks() -> list[ToDo]:
  return TASKS

def get_task(task_id: int) -> ToDo | None:
  for t in TASKS:
    if t.id == task_id:
      return t
  return None

def update_task(task_id: int, title: str | None = None, priority: str | None = None) -> bool: 
  t = get_task(task_id)
  if not t:
    return False
  if title is not None:
    title = title.strip()
    if title:
      t.title = title
  if priority is not None:
    p = priority.lower()
    if p in ALLOWED_PRIORITIES:
      t.priority = p
  return True

  
  





  