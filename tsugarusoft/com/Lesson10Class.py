class Pet:
    _pet_name: str
    _pet_age: int

    def __init__(self):
        self._pet_name = ""
        self._pet_age = 0

    def howling(self):
        print("ギャーギャー！")
        self._pet_name = "悪い子供、メッ！"
        return

    def handling(self):
        print("おなかなでなで")
        self._pet_name = "おーよしよしいい子だセッコ"

    def enjoyful_days(self):
        self._pet_age += 1

    def pets_age_is(self):
        return self._pet_age


class Dog(Pet):

        def __init__(self):
            self._pet_name = "ポチ太郎"
            self._pet_age = 4

        def howling(self):
            print("ワンワン！")
            self._pet_name = "悪い子供、メッ！"
            return

        def handling(self):
            print("おなかなでなで")
            self._pet_name = "おーよしよしいい子だポチヾ(｡>﹏<｡)ﾉﾞ✧*。 "

        def enjoyful_days(self):
            self._pet_age += 1 * 5

        def pets_age_is(self):
            return self._pet_age

class SiberianHusky(Dog):

    def __init__(self):
        self._pet_name = "ザンギエフ"
        self._pet_age = 2

    def enjoyful_days(self):
        self._pet_age += 1 * 2


myPet = SiberianHusky() #クラスをインスタンス化
myPet.howling() #メソッドを使ってみる
myPet.enjoyful_days() #幸せな日々を過ごす,犬は年を取るのが速い...
myPet.enjoyful_days()

print(myPet.pets_age_is()) #今の歳は？

print(myPet)#クラスを見てみる
