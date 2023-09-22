from callable_objects.constants.actions import Actions


def validate_input_datas(input_datas: list[str]) -> None:
    for input_data in input_datas:
        try:
            action = Actions(input_data)
        except ValueError:
            print(f'Wrong data: {input_data=}')
            continue

        print(action, type(action))
