from callable_objects.handlers_base.base_handler import BaseHandler
from callable_objects.storage.app_storage import get_app_storage


class SomeHandler1(BaseHandler):

    def do(self):
        app_storage = get_app_storage()

        print(f'Previous: { app_storage.latest_class_name=}')
        app_storage.latest_class_name = 'SomeHandler1'
        print(f'Current: { app_storage.latest_class_name=}')

        print(self.number * 2)
