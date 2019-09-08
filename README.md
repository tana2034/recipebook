# recipebook

参考にしたいレシピのリンクや画像を集めて見るためのWEBサイト

- プラットフォーム：heroku
- 言語：python3
- WEBフレームワーク：flask
- ORM: SQLAlchemy
- DB: postgreSQL
- 画像ファイル保存：dropbox
- DBマイグレーション：alembic
- ローカル環境：docker

## ローカル環境のセットアップ

```
git clone https://github.com/tana2034/recipebook.git
cd recipebook/docker
docker-compose up -d
```

## pytest実行

```
docker exec -it recipebook_python_1 bash
python -m pytest
```

## DB migration

```
# Create a Migration Script
alembic revision -m "create account table"

# Running Migration
alembic upgrade head

# Getting information
alembic current
```

## 画面のスクリーンショット

トップ画面

<img width="1438" alt="recipebook_top" src="https://user-images.githubusercontent.com/33181485/55273974-ffa60600-5315-11e9-8886-25ff80ecebfc.png">

レシピ登録画面

<img width="768" alt="recipebook_new" src="https://user-images.githubusercontent.com/33181485/55273973-ffa60600-5315-11e9-9c4f-57660fa1262d.png">
