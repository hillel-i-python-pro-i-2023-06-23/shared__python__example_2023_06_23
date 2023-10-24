import gc


def main():
    my_list = [1, 2, 3, 4, 5]

    my_new_list = [9, 8, my_list, 7, 6]

    print(my_list)

    print(locals())

    del my_list

    gc.collect()

    print(locals())

    print(my_list)  # noqa: F821


if __name__ == "__main__":
    main()
