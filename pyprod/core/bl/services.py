from .iservices import BaseUserService
from .irepository import BaseUserRepository
from .dto import UserDTO


class UserService(BaseUserService):
    def __init__(self, repository: BaseUserRepository):
        self.repository = repository

    def add(self, user: UserDTO) -> bool:
        return self.repository.add(user)

    def delete(self, user_id: int) -> bool:
        if not self.get_by_id(user_id):
            return False
        return self.repository.delete(user_id)

    def update(self, user: UserDTO) -> bool:
        if not self.get_by_id(user.id):
            return False
        return self.repository.update(user)

    def get_by_id(self, user_id: int) -> UserDTO:
        return self.repository.get_by_id(user_id)

    def get_by_username(self, username: str) -> UserDTO:
        return self.repository.get_by_username(username)

    def get_all(self) -> list[UserDTO]:
        return self.repository.get_all()

    def login(self, username: str, password: str) -> UserDTO:
        return self.repository.login(username, password)
