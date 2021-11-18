#文字列の出力
"""
文字列の出力を行うには 以下のようなprint関数を使用します。
()内の文字等が標準出力されます。
"""
print("hello world")


#ファイル/ライブラリの読み込み
"""
ファイル/ライブラリの読み込みはimport文を使用します。
import 名前

Ex. discord.pyを使いたい時は
import discord
"""
import library


#コメントアウト
"""
文字列をコメントアウトするには # を使用します。
コメントアウトされた行はコメントとして扱われます。
"""
print("hello world") #コメント
#コメント

#関数
"""
関数とはあるデータを受け取り、定められた独自の処理を実行し、その結果を返す命令のことです。
Pythonでの関数は async def ... / def ... のようになります。

- 同期関数
def 名前(引数):
    #処理
    
- 非同期関数
async def 名前(引数):
    #処理
"""
def test():
    #print("hello world")
    print("Hello World!")
