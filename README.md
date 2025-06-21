# TODO Web Application

シンプルで美しいTODOリスト管理アプリケーション

## 2つのバージョン

### 1. Flask版 (`app.py`)
- 従来のWebアプリケーション
- HTML/CSS/JavaScriptベースのUI
- RESTful API付き

### 2. Streamlit版 (`streamlit_app.py`)  
- モダンなWebアプリフレームワーク
- インタラクティブなUI
- Streamlit Cloud対応

## 特徴

- ✅ タスクの追加・削除・編集
- ✅ タスクの完了/未完了の切り替え
- ✅ モダンで美しいUI
- ✅ レスポンシブデザイン
- ✅ データの永続化（JSON）
- ✅ 統計情報の表示

## 技術スタック

- **Flask版**: Flask (Python) + HTML/CSS/JavaScript
- **Streamlit版**: Streamlit (Python)
- **Data Storage**: JSON ファイル

## セットアップ

### 1. リポジトリをクローン

```bash
git clone https://github.com/natsu0529/todo.git
cd todo
```

### 2. 仮想環境を作成・アクティベート

```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# または
venv\Scripts\activate     # Windows
```

### 3. 依存関係をインストール

```bash
pip install -r requirements.txt
```

## 実行方法

### Flask版を実行

```bash
python app.py
```

http://localhost:5001 でアクセス

### Streamlit版を実行

```bash
streamlit run streamlit_app.py
```

自動的にブラウザで開きます

## 🚨 緊急対応: ModuleNotFoundError (Flask)

**症状**: `ModuleNotFoundError: No module named 'flask'`

**原因**: Streamlit CloudでFlaskファイル（`app.py`）が実行されている

**即座の解決方法**:
1. Streamlit Cloud で「**Manage app**」→「**Settings**」をクリック
2. **Main file path** を `app.py` から `streamlit_app.py` に変更
3. 「**Save**」→「**Reboot app**」をクリック

**代替方法**: Main file path を `main.py` に設定

## 🔍 デバッグ: 何も表示されない場合

**症状**: Streamlit Cloudで画面が空白、または何も表示されない

**デバッグ手順**:
1. **Main file path**を一時的に `debug_app.py` に変更
2. デバッグ情報を確認
3. 正常動作を確認後、`streamlit_app.py` に戻す

**確認事項**:
- メインファイルが `streamlit_app.py` に設定されているか
- ブラウザのキャッシュをクリア
- 「Reboot app」を実行したか

### デプロイ手順

1. https://share.streamlit.io でアカウント作成
2. GitHubリポジトリを接続
3. **Main file path** に `streamlit_app.py` を指定
4. 自動的にデプロイされます

### トラブルシューティング

**エラー: "Error installing requirements"**

1. **Python バージョン**: `runtime.txt` で Python 3.10 を指定済み
2. **依存関係**: `requirements.txt` を最小限に設定 (`streamlit==1.28.1`)
3. **フォールバック**: エラーが続く場合は以下を試してください：
   - `requirements.txt` の内容を `streamlit` のみに変更
   - または `requirements-fallback.txt` の内容をコピー

**エラー: "This app has encountered an error"**
- メインファイルが `streamlit_app.py` に設定されているか確認
- `app.py` はFlask専用のため使用しないでください

**Streamlit Cloud設定確認手順**:
1. Streamlit Cloud ダッシュボードで「Manage app」をクリック
2. 「Settings」タブを選択
3. **Main file path**: `streamlit_app.py` を確認
4. **Python version**: `3.10` を確認
5. 「Save」をクリック後、「Reboot app」を実行

## API エンドポイント (Flask版のみ)

| メソッド | エンドポイント | 説明 |
|---------|------------|------|
| GET | `/` | メインページ |
| POST | `/add` | 新しいタスクを追加 |
| GET | `/toggle/<id>` | タスクの完了状態を切り替え |
| GET | `/delete/<id>` | タスクを削除 |
| GET | `/api/todos` | 全タスクをJSON形式で取得 |

## ファイル構成

```
todo/
├── app.py              # Flask版メインアプリ
├── streamlit_app.py    # Streamlit版メインアプリ
├── requirements.txt    # 依存関係
├── templates/
│   └── index.html     # Flask版HTMLテンプレート
├── todos.json         # データファイル（自動生成）
└── README.md          # このファイル
```

## ライセンス

MIT License
