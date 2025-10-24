from flask import Blueprint, render_template, redirect, url_for, request
from task import *

# Create a blueprint
main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/', methods=['GET', 'POST'])
def todo():
    if request.method == "POST":
        title = request.form.get("task-text", "").strip()
        priority = (request.form.get("priority") or "low").lower()
        if priority not in ALLOWED_PRIORITIES:
            priority = "low"
        if title:
            add_task(title, priority=priority)
        return redirect(url_for("main.todo"))
    # Show tasks
    return render_template("todo.html", tasks=get_tasks())

@main_blueprint.post("/toggle/<int:task_id>")
def toggle(task_id: int):
    toggle_task(task_id)
    return redirect(url_for("main.todo"))

@main_blueprint.post("/delete/<int:task_id>")
def delete(task_id: int):
    delete_task(task_id)
    return redirect(url_for("main.todo"))

@main_blueprint.route("/update/<int:task_id>", methods=["GET", "POST"])
def update(task_id: int):
    task = get_task(task_id)
    if request.method == "POST":
        title = request.form.get("task-text")
        priority = request.form.get("priority")
        ok = update_task(task_id, title=title, priority=priority)
        if not ok:
            return "There was a problem updating the task", 400
        return redirect(url_for("main.todo"))
    # GET: show edit form
    return render_template("update.html", task=task, allowed_priorities=sorted(ALLOWED_PRIORITIES))
    
