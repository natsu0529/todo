import streamlit as st
import json
import os
from datetime import datetime

# 基本的なページ設定
st.set_page_config(
    page_title="TODO アプリ",
    page_icon="📝",
    layout="centered"
)

# アプリタイトル
st.title("📝 TODO アプリ")
st.write("シンプルなタスク管理アプリです")

# TODO データファイル
TODO_FILE = 'todos.json'

def load_todos():
    """TODOデータを読み込む"""
    try:
        if os.path.exists(TODO_FILE):
            with open(TODO_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
    except Exception as e:
        st.error(f"データ読み込みエラー: {e}")
    return []

def save_todos(todos):
    """TODOデータを保存する"""
    try:
        with open(TODO_FILE, 'w', encoding='utf-8') as f:
            json.dump(todos, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        st.error(f"データ保存エラー: {e}")
        return False

# TODOリストを読み込み
todos = load_todos()

# 新しいTODOを追加
st.subheader("✨ 新しいタスクを追加")
with st.form("add_todo_form"):
    new_task = st.text_input("タスクを入力してください")
    submit_button = st.form_submit_button("追加")
    
    if submit_button and new_task:
        new_todo = {
            'id': max([todo.get('id', 0) for todo in todos], default=0) + 1,
            'task': new_task,
            'completed': False,
            'created_at': datetime.now().isoformat()
        }
        todos.append(new_todo)
        if save_todos(todos):
            st.success(f"「{new_task}」を追加しました！")
            st.rerun()

# TODOリストを表示
st.subheader("📋 タスク一覧")

if not todos:
    st.info("まだタスクがありません。新しいタスクを追加してください。")
else:
    for i, todo in enumerate(todos):
        col1, col2, col3 = st.columns([0.1, 0.7, 0.2])
        
        with col1:
            # 完了状態のチェックボックス
            completed = st.checkbox("", value=todo.get('completed', False), key=f"check_{todo['id']}")
            if completed != todo.get('completed', False):
                todos[i]['completed'] = completed
                save_todos(todos)
                st.rerun()
        
        with col2:
            # タスク内容
            if todo.get('completed', False):
                st.write(f"~~{todo['task']}~~")
            else:
                st.write(todo['task'])
        
        with col3:
            # 削除ボタン
            if st.button("🗑️", key=f"delete_{todo['id']}", help="削除"):
                todos = [t for t in todos if t['id'] != todo['id']]
                save_todos(todos)
                st.success("タスクを削除しました")
                st.rerun()

# 統計情報
if todos:
    completed_count = sum(1 for todo in todos if todo.get('completed', False))
    total_count = len(todos)
    st.write(f"📊 完了: {completed_count}/{total_count} タスク")

# フッター
st.write("---")
st.write("💡 **使い方**: 新しいタスクを追加し、完了したらチェックボックスをクリックしてください。")
