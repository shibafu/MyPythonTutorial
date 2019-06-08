def my_strategy1():
    print("1号の処理だぜ！")


def my_strategy2():
    print("2号の処理だぜ！")


my_strategy = my_strategy1
my_strategy()
my_strategy = my_strategy2
my_strategy()