# 📝 TODO アプリ

シンプルで美しいTODOアプリケーションです。FlaskとStreamlitの両方のバージョンを提供しています。

## 🚀 セットアップ

### 1. 仮想環境のセットアップ
```bash
# 仮想環境を自動セットアップ
./setup_venv.sh

# または手動で仮想環境を作成・有効化
python3 -m venv venv
source venv/bin/activate
```

### 2. 依存関係のインストール
```bash
# 仮想環境内でパッケージをインストール
source venv/bin/activate
pip install -r requirements.txt
```

## 🎯 実行方法

### Flask版（推奨）
```bash
# スクリプトで起動
./run_flask.sh

# または手動で起動
source venv/bin/activate
python flask_app.py
```
ブラウザで `http://localhost:8080` にアクセス

### Streamlit版
```bash
# スクリプトで起動
./run_streamlit.sh

# または手動で起動
source venv/bin/activate
streamlit run streamlit_app.py
```

## ✨ 機能

- ✅ タスクの追加
- ✅ タスクの完了/未完了切り替え
- ✅ タスクの削除
- ✅ データの永続化（JSON形式）
- ✅ 美しいレスポンシブUI

## 📁 プロジェクト構造

```
todo/
├── venv/                   # 仮想環境（自動生成）
├── templates/
│   └── index.html         # Flask用HTMLテンプレート
├── flask_app.py           # Flask版アプリ
├── streamlit_app.py       # Streamlit版アプリ
├── setup_venv.sh          # 仮想環境セットアップスクリプト
├── run_flask.sh           # Flask起動スクリプト
├── run_streamlit.sh       # Streamlit起動スクリプト
├── requirements.txt       # Python依存関係
└── todos.json            # データファイル（自動生成）
```

## 🔧 開発

**重要**: 常に仮想環境内で開発してください：
```bash
# 仮想環境を有効化
source venv/bin/activate

# 開発作業...

# パッケージ追加時
pip install package_name
pip freeze > requirements.txt
```

## 🌐 デプロイ

### Streamlit Cloud
- Main file path: `streamlit_app.py`
- Python version: 3.9+

### Heroku/Render
- Procfile と wsgi.py が設定済み
- Flask版が自動デプロイされます

## 💡 便利なスクリプト

- `./setup_venv.sh` - 仮想環境の初期セットアップ
- `./run_flask.sh` - Flask版の起動
- `./run_streamlit.sh` - Streamlit版の起動

---

🎯 **開発のポイント**: 必ず仮想環境内で作業を行い、依存関係を適切に管理してください。
