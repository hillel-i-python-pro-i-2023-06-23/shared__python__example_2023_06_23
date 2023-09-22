from abc import abstractmethod

from pydantic import BaseModel


class BaseHandler(BaseModel):
    number: int

    @abstractmethod
    def do(self):
        raise NotImplementedError

    def run(self):
        class_name = self.__class__.__name__

        print(f'start.{class_name}')

        self.do()
        print(f'end.{class_name}')
