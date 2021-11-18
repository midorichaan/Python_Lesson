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

async def test():
    await asyncio.sleep(3)


#データ型
"""
Pythonにはさまざまなデータ型があります。
str() → 文字列 'aiueo'
int() → 整数, 数値 5
float() → 浮動小数値, 小数 1.3
dict() → 辞書型 {}
list() → リスト型 []
tuple() → タプル型 ()
bool() → 真偽値 True False
"""
str() == "aiueo"
int() == 1
float() == 2.3
dict() == {}
list() == []
tuple() == ()
bool() == True, False
