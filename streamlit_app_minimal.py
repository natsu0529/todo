import streamlit as st
import json
import os
from datetime import datetime

# ページ設定
st.set_page_config(
    page_title="TODO アプリ",
    page_icon="📝",
    layout="centered"
)

# アプリタイトル
st.title("📝 TODO アプリ")

# TODO データファイル
TODO_FILE = 'todos.json'

def load_todos():
    """TODOデータを読み込む"""
    try:
        if os.path.exists(TODO_FILE):
            with open(TODO_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
    except:
        pass
    return []

def save_todos(todos):
    """TODOデータを保存する"""
    try:
        with open(TODO_FILE, 'w', encoding='utf-8') as f:
            json.dump(todos, f, ensure_ascii=False, indent=2)
    except:
        st.error("データの保存に失敗しました")

# TODOリストを読み込み
if 'todos' not in st.session_state:
    st.session_state.todos = load_todos()

# 新しいTODOを追加
st.subheader("✨ 新しいタスクを追加")
with st.form("add_todo_form"):
    new_task = st.text_input("タスクを入力してください")
    submit_button = st.form_submit_button("追加")
    
    if submit_button and new_task:
        new_id = max([todo.get('id', 0) for todo in st.session_state.todos], default=0) + 1
        new_todo = {
            'id': new_id,
            'task': new_task,
            'completed': False,
            'created_at': datetime.now().isoformat()
        }
        st.session_state.todos.append(new_todo)
        save_todos(st.session_state.todos)
        st.success(f"「{new_task}」を追加しました！")
        st.rerun()

# TODOリストを表示
st.subheader("📋 タスク一覧")

if not st.session_state.todos:
    st.info("まだタスクがありません。新しいタスクを追加してください。")
else:
    for i, todo in enumerate(st.session_state.todos):
        col1, col2, col3 = st.columns([0.1, 0.7, 0.2])
        
        with col1:
            # 完了状態のチェックボックス
            completed = st.checkbox("", value=todo.get('completed', False), key=f"check_{todo['id']}")
            if completed != todo.get('completed', False):
                st.session_state.todos[i]['completed'] = completed
                save_todos(st.session_state.todos)
                st.rerun()
        
        with col2:
            # タスク内容
            if todo.get('completed', False):
                st.write(f"~~{todo['task']}~~")
            else:
                st.write(todo['task'])
        
        with col3:
            # 削除ボタン
            if st.button("🗑️", key=f"delete_{todo['id']}"):
                st.session_state.todos = [t for t in st.session_state.todos if t['id'] != todo['id']]
                save_todos(st.session_state.todos)
                st.success("タスクを削除しました")
                st.rerun()

# 統計情報
if st.session_state.todos:
    completed_count = sum(1 for todo in st.session_state.todos if todo.get('completed', False))
    total_count = len(st.session_state.todos)
    st.write(f"📊 完了: {completed_count}/{total_count} タスク")
