# AutoDepositRakutenKeiba

楽天競馬に楽天銀行口座から100円振り込むプログラム

## 準備

以下はWindows環境にて

```
choco install -y python3
refreashenv

# (python3.4以降はすでにpipは含まれているらしい)
python -m pip install --upgrade pip
pip install selenium

# (chocoのツール用ディレクトリにseleniumクローム用ドライバー)
choco install -y selenium-chrome-driver

# 必要パッケージ
pip install python-dotenv
```

## `.env` ファイルの作成

楽天競馬へのログイン情報を環境変数ファイルに入力しておく．
以下は入力例

```
RakutenKeiba_ID = 楽天競馬のメールアドレス"
RakutenKeiba_PW = "楽天競馬のパスワード"
RakutenKeiba_PIN = "楽天競馬の振り込み用PINコード（半角数字 4桁）"
RakutenKeiba_DEP = "振込金額(半角数字 100推奨)"
```
