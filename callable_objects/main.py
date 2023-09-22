import enum


def some_func_1(number: int):
    print('some_func_1')
    print(number)


def some_func_2(number: int):
    print('some_func_2')
    print(number)


def some_func_3(number: int):
    print('some_func_3')
    print(number)


class Actions(enum.StrEnum):
    ACTION_1 = 'action_1'
    ACTION_2 = 'action_2'
    ACTION_3 = 'action_3'


#
REGISTRY: dict[Actions, callable] = {
    Actions.ACTION_1: some_func_1,
    Actions.ACTION_2: some_func_2,
    Actions.ACTION_3: some_func_3,
}

assert len(REGISTRY) == len(Actions), 'Not all actions in registry.'


def validate_input_datas(input_datas: list[str]) -> None:
    for input_data in input_datas:
        try:
            action = Actions(input_data)
        except ValueError:
            print(f'Wrong data: {input_data=}')
            continue

        print(action, type(action))


def main():
    input_datas = [
        'action_1',
    ]
    for input_data in input_datas:
        try:
            action = Actions(input_data)
        except ValueError:
            print(f'Wrong data: {input_data=}')
            continue

        func = REGISTRY[action]

        func(number=1)

    # datas = [
    #     'action_1',
    #     'wrong_data',
    # ]
    # validate_input_datas(input_datas=datas)

    # message = 'Hello'
    # code = f'print("{message}")'
    # exec(code)


if __name__ == "__main__":
    main()
