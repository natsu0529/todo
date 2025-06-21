# TODO Web Application

シンプルで美しいTODOリスト管理アプリケーション

## 特徴

- ✅ タスクの追加・削除・編集
- ✅ タスクの完了/未完了の切り替え
- ✅ モダンで美しいUI
- ✅ レスポンシブデザイン
- ✅ データの永続化（JSON）
- ✅ RESTful API

## 技術スタック

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Data Storage**: JSON ファイル

## セットアップ

### 1. リポジトリをクローン

```bash
git clone <repository-url>
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

### 4. アプリケーションを起動

```bash
python app.py
```

### 5. ブラウザでアクセス

http://localhost:5001 にアクセスしてアプリを使用できます。

## API エンドポイント

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
├── app.py              # メインアプリケーション
├── requirements.txt    # 依存関係
├── templates/
│   └── index.html     # HTMLテンプレート
├── todos.json         # データファイル（自動生成）
└── README.md          # このファイル
```

## ライセンス

MIT License
