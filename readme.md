# 天気情報表示Webアプリ

このアプリは、入力した都市名に基づいてOpenWeatherMap APIから天気情報を取得し、温度や天気説明を表示するWebアプリです。

![index](https://github.com/yut0takagi/weather_app/blob/main/img/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%202025-06-23%201.50.00.png)

---

## ✨ 使用技術

* Python 3.x
* Flask
* requests
* OpenWeatherMap API
* Tailwind CSS (CDN)

---

## ὎6 セットアップ方法

### 1. リポジトリをクローン

```bash
git clone https://github.com/yourusername/weather-app.git
cd weather-app
```

### 2. 仮想環境を作成して実行 (optional)

```bash
python -m venv venv
source venv/bin/activate  # Windowsの場合: venv\Scripts\activate
```

### 3. 依存パッケージをインストール

```bash
pip install -r requirements.txt
```

### 4. OpenWeatherMap API Key を設定

[https://openweathermap.org/](https://openweathermap.org/) で無料アカウント作成後、API key を main.py の中の `API_KEY` に設定

```python
API_KEY = "your_actual_api_key_here"
```

### 5. 実行

```bash
python main.py
```

ブラウザで [http://127.0.0.1:5000/](http://127.0.0.1:5000/) にアクセス

---

## ☁ 使い方

1. 都市名 (Tokyo など) を入力
2. 「天気を調べる」をクリック
3. 天気の情報 (温度、説明、アイコン) が表示

---

## 📁 ファイル構成

```
weather_app/
├── main.py              # Flask本体
├── requirements.txt     # 依存パッケージ
└── templates/
    └── index.html       # Tailwind適用温度表示UI
```

---

## 📈 拡張アイデア

* 3日分の予報に対応
* 地図表示 Google Maps 連携
* 温度グラフの表示
* 言語切り替え(英語/日本語)

---
