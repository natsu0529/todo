from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import os

app = Flask(__name__)

# TODOデータを保存するファイル
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

@app.route('/')
def index():
    """メインページ"""
    todos = load_todos()
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    """新しいTODOを追加"""
    task = request.form.get('task')
    if task:
        todos = load_todos()
        new_todo = {
            'id': len(todos) + 1,
            'task': task,
            'completed': False
        }
        todos.append(new_todo)
        save_todos(todos)
    return redirect(url_for('index'))

@app.route('/toggle/<int:todo_id>')
def toggle_todo(todo_id):
    """TODOの完了状態を切り替え"""
    todos = load_todos()
    for todo in todos:
        if todo['id'] == todo_id:
            todo['completed'] = not todo['completed']
            break
    save_todos(todos)
    return redirect(url_for('index'))

@app.route('/delete/<int:todo_id>')
def delete_todo(todo_id):
    """TODOを削除"""
    todos = load_todos()
    todos = [todo for todo in todos if todo['id'] != todo_id]
    save_todos(todos)
    return redirect(url_for('index'))

@app.route('/api/todos')
def api_todos():
    """API: TODOリストを取得"""
    todos = load_todos()
    return jsonify(todos)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
