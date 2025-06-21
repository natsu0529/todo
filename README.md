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

## Streamlit Cloudでのデプロイ

1. GitHubリポジトリをStreamlit Cloudに接続
2. `streamlit_app.py`をメインファイルとして指定
3. 自動的にデプロイされます

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
