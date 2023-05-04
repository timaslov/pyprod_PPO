import pytest


from ..da import User, UserRepository
from ..bl import UserDTO


@pytest.mark.django_db
def test_delete_user():
    user = User.objects.create_user(
        username="timaslov",
        email="timaslov@mail.ru",
        password="12345",
    )
    res = UserRepository().delete(user.id)
    users_count = User.objects.count()
    assert res
    assert users_count == 0


@pytest.mark.django_db
def test_get_user_by_id():
    user_dto = UserDTO(
        username="timaslov",
        first_name="Тихон",
        last_name="Маслов",
        email="timaslov@mail.ru",
        password="12345",
    )
    user = User.objects.create_user(
        username=user_dto.username,
        first_name=user_dto.first_name,
        last_name=user_dto.last_name,
        email=user_dto.email,
        password=user_dto.password,
    )
    res = UserRepository().get_by_id(user.id)
    assert user_dto.username == res.username
    assert user_dto.first_name == res.first_name
    assert user_dto.last_name == res.last_name
    assert user_dto.email == res.email
