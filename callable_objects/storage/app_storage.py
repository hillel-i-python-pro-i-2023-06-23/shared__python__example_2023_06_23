from callable_objects.storage.app_storage_class import AppStorage

app_storage = AppStorage()


def get_app_storage() -> AppStorage:
    return app_storage
