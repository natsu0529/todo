import streamlit as st
import json
import os
from datetime import datetime

# デバッグ: アプリが読み込まれていることを確認
st.write("🔄 streamlit_app.pyが読み込まれました")

# ページ設定
st.set_page_config(
    page_title="TODO アプリ",
    page_icon="📝",
    layout="centered"
)

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

def add_todo(task):
    """新しいTODOを追加"""
    todos = load_todos()
    new_todo = {
        'id': max([todo['id'] for todo in todos], default=0) + 1,
        'task': task,
        'completed': False,
        'created_at': datetime.now().isoformat()
    }
    todos.append(new_todo)
    save_todos(todos)

def toggle_todo(todo_id):
    """TODOの完了状態を切り替え"""
    todos = load_todos()
    for todo in todos:
        if todo['id'] == todo_id:
            todo['completed'] = not todo['completed']
            break
    save_todos(todos)

def delete_todo(todo_id):
    """TODOを削除"""
    todos = load_todos()
    todos = [todo for todo in todos if todo['id'] != todo_id]
    save_todos(todos)

# メインアプリ
def main():
    st.title("📝 TODO アプリ")
    st.markdown("### あなたのタスクを効率的に管理しましょう")
    
    # 新しいタスクの追加
    st.markdown("---")
    with st.form("add_todo_form"):
        new_task = st.text_input("新しいタスクを入力してください", placeholder="例: 買い物に行く")
        submit_button = st.form_submit_button("追加", use_container_width=True)
        
        if submit_button and new_task:
            add_todo(new_task)
            st.success(f"タスク「{new_task}」を追加しました！")
            st.rerun()
    
    # TODOリストの表示
    st.markdown("---")
    todos = load_todos()
    
    if not todos:
        st.info("📋 タスクがありません。上のフォームから新しいタスクを追加してください。")
        return
    
    # 統計情報
    total_todos = len(todos)
    completed_todos = len([todo for todo in todos if todo['completed']])
    pending_todos = total_todos - completed_todos
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("総タスク数", total_todos)
    with col2:
        st.metric("完了", completed_todos)
    with col3:
        st.metric("未完了", pending_todos)
    
    st.markdown("---")
    st.markdown("### タスク一覧")
    
    # TODOアイテムの表示
    for todo in todos:
        col1, col2, col3 = st.columns([0.1, 0.7, 0.2])
        
        with col1:
            # チェックボックス
            is_completed = st.checkbox("", value=todo['completed'], key=f"check_{todo['id']}")
            if is_completed != todo['completed']:
                toggle_todo(todo['id'])
                st.rerun()
        
        with col2:
            # タスクテキスト
            if todo['completed']:
                st.markdown(f"~~{todo['task']}~~")
            else:
                st.markdown(todo['task'])
        
        with col3:
            # 削除ボタン
            if st.button("🗑️", key=f"delete_{todo['id']}", help="削除"):
                delete_todo(todo['id'])
                st.rerun()
    
    # 全て完了したタスクを削除するボタン
    if completed_todos > 0:
        st.markdown("---")
        if st.button("完了したタスクをすべて削除", type="secondary"):
            todos = load_todos()
            todos = [todo for todo in todos if not todo['completed']]
            save_todos(todos)
            st.success(f"{completed_todos}個の完了タスクを削除しました！")
            st.rerun()

if __name__ == "__main__":
    main()
