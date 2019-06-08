import sys


def _none_calc():
    _calcNum = 24 + 29  # Nullオブジェクトと無理矢理足し算する。これは例外

    print(_calcNum)
    raise TypeError("テストで発生したエラーです")


try:
    _none_calc()
except TypeError as e:
    print("Noneとint型は足し算できません！ {0}".format(e.args))
except OSError as e:
    print("ここはデッドコード")
