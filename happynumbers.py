def happy(number):

    next_ = sum((int(char) ** 2 for char in str(number)))
    return number in (1,7) if number < 10 else happy(next_)


assert happy(1)
assert happy(10)
assert happy(100)
assert happy(130)
assert happy(97)
assert not happy(4)