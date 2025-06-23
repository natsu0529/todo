import streamlit as st
import json
import os
from datetime import datetime

# ページ設定
st.set_page_config(
    page_title="📝 TODO アプリ",
    page_icon="📝",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# カスタムCSS
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #667eea;
        margin-bottom: 2rem;
    }
    
    .todo-item {
        padding: 1rem;
        margin: 0.5rem 0;
        border-radius: 10px;
        border: 1px solid #e0e0e0;
        background-color: #f9f9f9;
    }
    
    .completed-task {
        text-decoration: line-through;
        color: #888;
        background-color: #e8f5e8;
    }
    
    .stats {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# アプリタイトル
st.markdown('<h1 class="main-header">📝 TODO アプリ</h1>', unsafe_allow_html=True)
st.markdown("### シンプルで美しいタスク管理")

# TODO データファイル
TODO_FILE = 'todos.json'

def load_todos():
    """TODOデータを読み込む"""
    try:
        if os.path.exists(TODO_FILE):
            with open(TODO_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data if isinstance(data, list) else []
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

# セッション状態の初期化
if 'todos' not in st.session_state:
    st.session_state.todos = load_todos()

if 'refresh_counter' not in st.session_state:
    st.session_state.refresh_counter = 0

# 新しいTODO追加セクション
st.markdown("---")
st.subheader("✨ 新しいタスクを追加")

col1, col2 = st.columns([4, 1])

with col1:
    new_task = st.text_input(
        "タスクを入力してください", 
        placeholder="例: 買い物に行く",
        key="new_task_input"
    )

with col2:
    add_button = st.button("➕ 追加", type="primary", use_container_width=True)

if add_button and new_task.strip():
    # 新しいIDを生成
    existing_ids = [todo.get('id', 0) for todo in st.session_state.todos]
    new_id = max(existing_ids, default=0) + 1
    
    new_todo = {
        'id': new_id,
        'task': new_task.strip(),
        'completed': False,
        'created_at': datetime.now().isoformat(),
        'updated_at': datetime.now().isoformat()
    }
    
    st.session_state.todos.append(new_todo)
    
    if save_todos(st.session_state.todos):
        st.success(f"✅ 「{new_task}」を追加しました！")
        # 入力フィールドをクリア
        st.session_state.new_task_input = ""
        st.session_state.refresh_counter += 1
        st.rerun()
    else:
        st.error("❌ タスクの追加に失敗しました")

# TODOリスト表示セクション
st.markdown("---")
st.subheader("📋 タスク一覧")

if not st.session_state.todos:
    st.info("📝 まだタスクがありません。上記のフォームから新しいタスクを追加してください。")
else:
    # 統計情報
    total_tasks = len(st.session_state.todos)
    completed_tasks = sum(1 for todo in st.session_state.todos if todo.get('completed', False))
    pending_tasks = total_tasks - completed_tasks
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("📊 総タスク数", total_tasks)
    with col2:
        st.metric("✅ 完了", completed_tasks)
    with col3:
        st.metric("⏳ 未完了", pending_tasks)
    
    st.markdown("---")
    
    # タスクを表示
    for i, todo in enumerate(st.session_state.todos):
        task_id = todo.get('id', i)
        task_text = todo.get('task', '')
        is_completed = todo.get('completed', False)
        
        # タスクのコンテナ
        with st.container():
            col1, col2, col3 = st.columns([0.1, 0.7, 0.2])
            
            with col1:
                # 完了チェックボックス
                completed = st.checkbox(
                    "", 
                    value=is_completed, 
                    key=f"check_{task_id}_{st.session_state.refresh_counter}",
                    help="完了/未完了を切り替え"
                )
                
                # 状態が変更された場合
                if completed != is_completed:
                    st.session_state.todos[i]['completed'] = completed
                    st.session_state.todos[i]['updated_at'] = datetime.now().isoformat()
                    
                    if save_todos(st.session_state.todos):
                        status = "完了" if completed else "未完了"
                        st.success(f"✅ タスクを{status}に変更しました")
                        st.session_state.refresh_counter += 1
                        st.rerun()
            
            with col2:
                # タスク内容
                if is_completed:
                    st.markdown(f"~~{task_text}~~ ✅")
                else:
                    st.markdown(f"**{task_text}**")
                
                # 作成日時を小さく表示
                created_at = todo.get('created_at', '')
                if created_at:
                    try:
                        created_time = datetime.fromisoformat(created_at.replace('Z', '+00:00'))
                        st.caption(f"作成: {created_time.strftime('%Y-%m-%d %H:%M')}")
                    except:
                        pass
            
            with col3:
                # 削除ボタン
                if st.button(
                    "🗑️ 削除", 
                    key=f"delete_{task_id}_{st.session_state.refresh_counter}",
                    help="このタスクを削除",
                    type="secondary"
                ):
                    # タスクを削除
                    st.session_state.todos = [
                        t for t in st.session_state.todos 
                        if t.get('id') != task_id
                    ]
                    
                    if save_todos(st.session_state.todos):
                        st.success(f"🗑️ 「{task_text}」を削除しました")
                        st.session_state.refresh_counter += 1
                        st.rerun()
                    else:
                        st.error("❌ タスクの削除に失敗しました")
        
        st.markdown("---")

# フッター
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; margin-top: 2rem;">
    <p>💡 <strong>使い方</strong>: 新しいタスクを追加 → チェックボックスで完了マーク → 不要なタスクを削除</p>
    <p>🎯 シンプルで効率的なタスク管理を実現</p>
</div>
""", unsafe_allow_html=True)

# デバッグ情報（開発時のみ）
if st.sidebar.checkbox("🔧 デバッグ情報を表示"):
    st.sidebar.write("### デバッグ情報")
    st.sidebar.write(f"総タスク数: {len(st.session_state.todos)}")
    st.sidebar.write(f"リフレッシュ回数: {st.session_state.refresh_counter}")
    st.sidebar.write(f"データファイル存在: {os.path.exists(TODO_FILE)}")
    
    if st.sidebar.button("🔄 データを再読み込み"):
        st.session_state.todos = load_todos()
        st.session_state.refresh_counter += 1
        st.rerun()
        
    if st.sidebar.button("🗑️ 全データクリア"):
        st.session_state.todos = []
        save_todos([])
        st.session_state.refresh_counter += 1
        st.rerun()
