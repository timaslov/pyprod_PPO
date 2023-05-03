from abc import ABC, abstractmethod

from .dto import UserDTO


class BaseUserRepository(ABC):
    @abstractmethod
    def add(self, user: UserDTO) -> bool:
        """ Добавить нового юзера """

    @abstractmethod
    def delete(self, user_id: int) -> bool:
        """ Удалить юзера """

    @abstractmethod
    def update(self, user: UserDTO) -> bool:
        """ Обновить юзера """

    @abstractmethod
    def get_by_id(self, user_id: int) -> UserDTO | None:
        """ Получить юзера по id """

    @abstractmethod
    def get_by_username(self, username: str) -> UserDTO | None:
        """ Получить юзера по username-у """

    @abstractmethod
    def get_all(self) -> list[UserDTO]:
        """ Получить всех юзеров """

    @abstractmethod
    def login(self, username: str, password: str) -> UserDTO:
        """ Аутентифицировать юзера """
