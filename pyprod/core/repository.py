from dataclasses import asdict

from django.contrib.auth import authenticate

from .irepository import BaseUserRepository
from .dto import UserDTO
from .models import User


class UserRepository(BaseUserRepository):
    def add(self, user: UserDTO) -> bool:
        return User.objects.create(**asdict(user))

    def delete(self, user_id: int) -> bool:
        return User.objects.delete(pk=user_id)

    def update(self, user: UserDTO) -> bool:
        return User.objects.update(**asdict(user))

    def get_by_id(self, user_id: int) -> UserDTO | None:
        return User.objects.filter(pk=user_id).first()

    def get_by_username(self, username: str) -> UserDTO | None:
        return User.objects.filter(pk=username).first()

    def get_all(self) -> list[UserDTO]:
        return User.objects.all()

    def login(self, username: str, password: str) -> UserDTO:
        return authenticate(username=username, password=password)
