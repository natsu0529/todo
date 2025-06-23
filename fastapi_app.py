from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse
import json
import os
from datetime import datetime

app = FastAPI(title="TODO アプリ")
templates = Jinja2Templates(directory="templates")

# TODO データファイル
TODO_FILE = 'todos.json'

def load_todos():
    """TODOデータを読み込む"""
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_todos(todos):
    """TODOデータを保存する"""
    with open(TODO_FILE, 'w', encoding='utf-8') as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """メインページ"""
    todos = load_todos()
    return templates.TemplateResponse("index.html", {
        "request": request, 
        "todos": todos
    })

@app.post("/add")
async def add_todo(task: str = Form(...)):
    """新しいTODOを追加"""
    if task:
        todos = load_todos()
        new_todo = {
            'id': max([todo['id'] for todo in todos], default=0) + 1,
            'task': task,
            'completed': False,
            'created_at': datetime.now().isoformat()
        }
        todos.append(new_todo)
        save_todos(todos)
    return RedirectResponse(url="/", status_code=303)

@app.get("/toggle/{todo_id}")
async def toggle_todo(todo_id: int):
    """TODOの完了状態を切り替え"""
    todos = load_todos()
    for todo in todos:
        if todo['id'] == todo_id:
            todo['completed'] = not todo['completed']
            break
    save_todos(todos)
    return RedirectResponse(url="/", status_code=303)

@app.get("/delete/{todo_id}")
async def delete_todo(todo_id: int):
    """TODOを削除"""
    todos = load_todos()
    todos = [todo for todo in todos if todo['id'] != todo_id]
    save_todos(todos)
    return RedirectResponse(url="/", status_code=303)

@app.get("/health")
async def health_check():
    """ヘルスチェック"""
    return {"status": "ok", "message": "FastAPI TODO App is running"}

if __name__ == "__main__":
    import uvicorn
    print("🚀 FastAPI TODO アプリを起動中...")
    print("📝 ブラウザで http://localhost:8000 にアクセスしてください")
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
