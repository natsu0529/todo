# Streamlit環境での実行を完全に防ぐ
import os
import sys

# 最初にStreamlit環境をチェック
if ('streamlit' in sys.modules or 
    'STREAMLIT_SERVER_PORT' in os.environ or 
    any(key.startswith('STREAMLIT_') for key in os.environ.keys()) or
    '/mount/src/' in os.getcwd() or  # Streamlit Cloud特有のパス
    'adminuser' in os.getcwd()):     # Streamlit Cloud特有のユーザー
    
    print("🚫 このファイル(app.py)はStreamlit環境では実行できません")
    print("✅ 代わりに 'streamlit_app.py' を使用してください")
    print("⚙️  Streamlit Cloud設定: Main file path を 'streamlit_app.py' に変更してください")
    sys.exit(1)

from flask import Flask, render_template, request, redirect, url_for, jsonify
import json

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
    # Streamlit環境では実行しない - より確実な検出方法
    import sys
    
    # Streamlit環境の検出
    if 'streamlit' in sys.modules or 'STREAMLIT_SERVER_PORT' in os.environ:
        print("❌ Streamlit環境が検出されました。")
        print("🔄 このファイル(app.py)はFlask専用です。")
        print("✅ Streamlit版を使用するには 'streamlit_app.py' を実行してください。")
        sys.exit(0)
    
    # Streamlit Cloudの環境変数をチェック
    if any(key.startswith('STREAMLIT_') for key in os.environ.keys()):
        print("❌ Streamlit Cloud環境が検出されました。")
        print("🔄 streamlit_app.py を使用してください。")
        sys.exit(0)
    
    print("✅ Flask環境で実行中...")
    
    # Flask環境でのみ実行
    port = int(os.environ.get('PORT', 5001))
    debug = os.environ.get('FLASK_ENV') != 'production'
    app.run(debug=debug, host='0.0.0.0', port=port)
