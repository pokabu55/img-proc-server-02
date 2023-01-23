# img-proc-server-02
画像処理サーバー
ラズパイにサーバーを置くことを前提
一旦、ブワッと書くだけなので、後で修正必須だな。

# ラズパイの開発架橋
## 使用モデル
* 3b（＋じゃない）

## リモート開発環境
* SSH と VNC は有効にしておく
* 念の為、`sudo apt update` と `sudo apt upgrade` を実行しておく

## IPアドレスの固定
* [ここ](https://mugeek.hatenablog.com/entry/2019/05/27/230256)を参照した
* IPアドレスは、ルーターでDHCPの予約分があるから、かぶらないようにする

# ローカルの環境設定
## SSH 接続
* 端末で、 `ssh ラズパイのユーザー名@xxx.xxx.xxx.xxx` xは数字でIPアドレスのこと
* 端末でやめるときって `exit` って打つの、初めて知った。

## SSHFS 接続
* SSH接続したリモートのディレクトリをマウントしてくれる機能って、説明であってるのかな？
* 端末で、 `sshfs ラズパイのユーザー名@xxx.xxx.xxx.xxx:/home/ユーザー名 マウントしたいローカルのパス`
* 成功すると、nautilus 上に、外付けドライブのように表示されます。
* [ここ](https://developers.gmo.jp/18603/)を読むと、sshfsはすでに開発終了となっているので、他の方法が説明してある

# ラズパイ側のサーバーの設定
## Apache
* [ここ](https://www.fabshop.jp/webserver-apache/)を見てインストール
* 実行も問題なかった

## streamlit
* [ここ](https://hitori-sekai.com/python/error-streamlit-install/)を見た
* ラズパイだと、0.62.0 じゃないと動かないって書いてあった
* 確かに、最新を入れたら起動しなかった
* pip で 0.62.0 をインストールし直したら、動いた
* 確認は、`streamlit hello` でサーバー起動。ローカルマシンで画面を確認できた

## flet
* [ここ](https://qiita.com/NasuPanda/items/48849d7f925784d6b6a0)を見た
* が、こっちままだ試せてない

# その他
ちょっと大変だったので、メモします。
* git を ラズパイで使うには
 * githubの設定で、ラズパイで設定した公開鍵をgithubにコピーする必要がある
 * このあたりの話は、以下を参照とした。キーのクリップボードへのコピー方法もね。
 * [ここ](https://qiita.com/shizuma/items/2b2f873a0034839e47ce) と [ここ](https://qiita.com/Kzno/items/6f2fa98256bdffb0fd43)
 
* VSCODEで、リモートにSSHで入って、開発する方法
 * [ここ](https://tec.tecotec.co.jp/entry/2021/12/11/000000)を見た
 
