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


#基本のメソッド/組み込み関数
"""
よく使われる関数やメソッドの一覧です。
"""
#組み込み関数
print() #()内の物を出力する
str() #str (文字)のオブジェクトを返す
int() #int (数値)のオブジェクトを返す
float() #float (小数)のオブジェクトを返す
bool() #bool値を返す。 空や0、NoneはFalseを返す
type() #()内のオブジェクトの型を返す
input() #文字列を入力する (入力された値は文字列扱いになる)
len() #()内の要素の数を返す
abs() #()内の数値の絶対値を返す
sum() #()内の数値の合計値を返す
max() #()内の数値の最大値を返す
min() #()内の数値の最小値を返す
pow(a, b) #() aのb乗を返す
range(a, b, c) #指定範囲の整数列を返す aからb, c倍数
hex() #16進数を返す
oct() #8進数を返す
bin() #2進数を返す
enumerate() #シーケンスとインデックスを取得する。第二引数はインデックスの開始ナンバーで、デフォルトは0
open() #ファイルを開く
eval() #文字列を評価する
exec() #pythonコードの動的な実行

#関数
.append() #リスト型で末尾に要素を追加する
.extend() #リスト型の末尾にシーケンスを追加する
.reverse() #リスト内要素の順番を逆にする
.sort() #リスト内要素を並べ替える
.remove() #リスト内の指定した値と同じ要素を削除する
.count() #リスト、タプル型の指定要素がいくつ含まれるか返す
.pop() #リスト、辞書型の指定インデックスの要素を取り出して削除する
.clear() #リスト、辞書型の全ての要素を削除する
.keys() #辞書型の全てのキーを返す
.values() #辞書型の全ての要素を返す
.items() #辞書型の全てのキーと要素を返す
.upper() #文字列を大文字に変換
.lower() #文字列を小文字に変換
.capitalize() #最初の文字を大文字に、残りの文字を小文字に変換
.replace(a, b) #文字列のaをbに置き換え
.split() #文字列を特定の文字で分割
.join(シーケンス) #連結した文字列を得る
.index() #指定した文字がある位置のインデックスを返す
.format() #{}内のものを()内で置き換える


#Pythonファイル
"""
Pythonのファイルは基本 名前.py になります
よくあるのが必要なモジュールと一緒の名前になってimportした時にエラーになること。

ちなみにこのファイル、プログラムはターミナルから python3 名前.py または py -3 名前.py で実行できるよ！
"""
