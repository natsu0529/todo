import streamlit as st
import json
import os
from datetime import datetime

# ページ設定を最初に実行（Streamlit要件）
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
        try:
            with open(TODO_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            return []
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

def add_todo(task):
    """新しいTODOを追加"""
    todos = load_todos()
    new_todo = {
        'id': max([todo.get('id', 0) for todo in todos], default=0) + 1,
        'task': task,
        'completed': False,
        'created_at': datetime.now().isoformat()
    }
    todos.append(new_todo)
    return save_todos(todos)

def toggle_todo(todo_id):
    """TODOの完了状態を切り替え"""
    todos = load_todos()
    for todo in todos:
        if todo.get('id') == todo_id:
            todo['completed'] = not todo.get('completed', False)
            break
    return save_todos(todos)

def delete_todo(todo_id):
    """TODOを削除"""
    todos = load_todos()
    todos = [todo for todo in todos if todo.get('id') != todo_id]
    return save_todos(todos)

# セッション状態の初期化
if 'refresh_trigger' not in st.session_state:
    st.session_state.refresh_trigger = 0

# メインアプリ
st.title("📝 TODO アプリ")
st.markdown("### あなたのタスクを効率的に管理しましょう")

# 新しいタスクの追加
st.markdown("---")
with st.form("add_todo_form"):
    new_task = st.text_input("新しいタスクを入力してください", placeholder="例: 買い物に行く")
    submit_button = st.form_submit_button("追加", use_container_width=True)
    
    if submit_button and new_task.strip():
        if add_todo(new_task.strip()):
            st.success(f"タスク「{new_task}」を追加しました！")
            st.session_state.refresh_trigger += 1
            st.rerun()

# TODOリストの表示
st.markdown("---")
todos = load_todos()

if not todos:
    st.info("📋 タスクがありません。上のフォームから新しいタスクを追加してください。")
else:
    # 統計情報
    total_todos = len(todos)
    completed_todos = sum(1 for todo in todos if todo.get('completed', False))
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
    for i, todo in enumerate(todos):
        todo_id = todo.get('id', i)
        task_text = todo.get('task', '不明なタスク')
        is_completed = todo.get('completed', False)
        
        col1, col2, col3 = st.columns([0.1, 0.7, 0.2])
        
        with col1:
            # チェックボックス
            checkbox_key = f"check_{todo_id}_{st.session_state.refresh_trigger}"
            new_completed = st.checkbox("", value=is_completed, key=checkbox_key)
            if new_completed != is_completed:
                if toggle_todo(todo_id):
                    st.session_state.refresh_trigger += 1
                    st.rerun()
        
        with col2:
            # タスクテキスト
            if is_completed:
                st.markdown(f"~~{task_text}~~")
            else:
                st.markdown(task_text)
        
        with col3:
            # 削除ボタン
            delete_key = f"delete_{todo_id}_{st.session_state.refresh_trigger}"
            if st.button("🗑️", key=delete_key, help="削除"):
                if delete_todo(todo_id):
                    st.session_state.refresh_trigger += 1
                    st.rerun()

    # 全て完了したタスクを削除するボタン
    if completed_todos > 0:
        st.markdown("---")
        clear_key = f"clear_completed_{st.session_state.refresh_trigger}"
        if st.button("完了したタスクをすべて削除", type="secondary", key=clear_key):
            todos = load_todos()
            active_todos = [todo for todo in todos if not todo.get('completed', False)]
            if save_todos(active_todos):
                st.success(f"{completed_todos}個の完了タスクを削除しました！")
                st.session_state.refresh_trigger += 1
                st.rerun()
