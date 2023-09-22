from callable_objects.constants.actions import Actions
from callable_objects.constants.actions_registry import REGISTRY


def main():
    input_datas = [
        "action_1",
        "action_2",
    ]

    for input_data in input_datas:
        try:
            action = Actions(input_data)
        except ValueError:
            print(f"Wrong data: {input_data=}")
            continue

        handler_class = REGISTRY[action]

        handler = handler_class(number=1)
        handler.run()

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
