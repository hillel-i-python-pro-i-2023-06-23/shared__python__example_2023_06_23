# TODO ? Rework AppStorage to singleton ? Because we want to ensure that only one instance of AppStorage exists.
#  But we can have problems with multiprocessing,  if we need to edit AppStorage in different processes.
#  So we need to use some synchronization mechanism, if we want to use multiprocessing.
#  https://refactoring.guru/ru/design-patterns/singleton/python/example#example-1

class AppStorage:

    def __init__(self):
        self._latest_class_name = None
        print('model_post_init')

    @property
    def latest_class_name(self) -> str | None:
        print('latest_class_name.getter')
        return self._latest_class_name

    @latest_class_name.setter
    def latest_class_name(self, value: str):
        print('latest_class_name.setter')
        self._latest_class_name = value
