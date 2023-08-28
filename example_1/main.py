import pathlib
from dataclasses import dataclass
from typing import Final

ROOT_DIR: Final[pathlib.Path] = pathlib.Path(__file__).parent

name1 = 'name1'
list_1 = [1, 2, 3]


@dataclass
class Storage:
    value: str | None = None
    # some_list: list = Field(default_factory=list)


storage = Storage()


@dataclass
class Human:
    name: str
    age: int


def make_string_1(name: str):
    name = name.lower()
    return name


def make_list_1(lst: list):
    lst.append(1)
    return lst


def make_string_2(name: str):
    ROOT_DIR.joinpath('main.py')
    name += '1'
    return name


def some_action_1():
    print(storage.value)
    storage.value = '1'
    print(storage.value)


def edit_human(human: Human) -> None:
    human.age = 10


def some_generator():
    for i in range(10):
        yield i


def main():
    name2 = make_string_1(name=name1)

    list_2 = make_list_1(lst=list_1)

    human = Human(name='name', age=20)
    print(human)
    edit_human(human=human)
    print(human)

    some = some_generator()

    ...


if __name__ == '__main__':
    main()
