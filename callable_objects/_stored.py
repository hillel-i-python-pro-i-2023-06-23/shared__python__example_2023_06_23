def some_func_1(number: int):
    print("some_func_1")
    print(number)


def some_func_2(number: int):
    print("some_func_2")
    print(number)


def some_func_3(number: int):
    print("some_func_3")
    print(number)


def example_1():
    input_data = "action_1"

    if input_data == "action_1":
        func = some_func_1
    elif input_data == "action_2":
        func = some_func_2
    elif input_data == "action_3":
        func = some_func_3
    else:
        raise ValueError

    print(f"{func.__name__=}")
    print(func.__annotations__)
    print(func.__code__.co_varnames)
    print(func.__code__.co_argcount)

    func(number=1)


if __name__ == "__main__":
    example_1()
