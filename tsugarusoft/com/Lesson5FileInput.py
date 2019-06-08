"""
自分で定義した関数
@author わたし＾ｐ＾
"""
def input_method() -> str:
    return input("こんにちわ！\r\n")


myStrategy: input_method = input_method  #関数オブジェクトを作成する。オブジェクトの型は関数名になる。
greeting_message: str = myStrategy() #自由に入れ替えた関数オブジェクトを実行する
print(greeting_message)