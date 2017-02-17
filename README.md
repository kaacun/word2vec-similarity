# Word2vecのセットアップ
## 環境構築
Macにpyenvでpython2.7環境を作り、動作させています。

### pythonのパッケージ管理ツールpipをインストール
`easy_install pip`

### gensimをインストール
`pip install --upgrade gensim`

### mecabインストール
`brew install mecab `
`brew install mecab-ipadic `

## 学習データの準備(wikipedia)
wikipediaを学習データとして用意する方法について書く。

### Wikipediaデータのダウンロード
`wget http://dumps.wikimedia.org/jawiki/latest/jawiki-latest-pages-articles.xml.bz2`

- ２GB、2時間以上かかるので注意！

### Rubyインストール
このあとのwp2txtを利用するのに必要。  
rbenvとかで適当に入れる。

### wp2txtインストール
`gem install wp2txt `

### wikipediaデータをwp2txtにかける
`wp2txt --input-file jawiki-latest-pages-articles.xml.bz2 `

- かなり時間かかるので注意！スペックの高いマシンでやった方がいい。

### wp2txtの結果を結合
`cat jawiki-latest-pages-articles.xml-* > corpus.txt `

### mecabを使って分かち書きする
`mecab -b 100000 -Owakati corpus.txt -o corpus_wakati.txt `

- それなりに時間がかかるので注意！

## 学習
`python training.py`

たったこれだけのコードでできてしまう。
学習はやはりそれなりに時間がかかる。

# 学習結果の確認
`python similarity.py`

```py
model.similarity(u"ステーキ", u"焼肉")
0.802548346712
model.similarity(u"ステーキ", u"サーロイン")
0.727586288732
model.similarity(u"ステーキ", u"野菜")
0.679391729492
model.similarity(u"ステーキ", u"ガスト")
0.554430442829
model.similarity(u"ステーキ", u"魚")
0.447672316625
model.similarity(u"ステーキ", u"ナイフ")
0.385388946857
```

# 参考

- [word2vecで遊ぶ](http://eyepodtouch.net/?p=77)
