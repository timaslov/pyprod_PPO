from dataclasses import asdict

from django.contrib.auth import authenticate

from ..bl import BaseUserRepository, UserDTO
from .models import User


class UserRepository(BaseUserRepository):
    def add(self, user: UserDTO) -> bool:
        return User.objects.create_user(
            username=user.username,
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            password=user.password,
        )

    def delete(self, user_id: int) -> bool:
        return User.objects.filter(pk=user_id).delete()

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
