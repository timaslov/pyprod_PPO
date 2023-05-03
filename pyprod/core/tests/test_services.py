import datetime

from ..dto import UserDTO
from ..services import UserService


def test_add_user(mocker):
    repository = mocker.Mock()
    user = UserDTO(
        username="timaslov",
        first_name="Тихон",
        last_name="Маслов",
        email="timaslov@mail.ru",
        id=7,
        password="12345",
        date_joined=datetime.datetime(2022, 5, 7, 13, 26),
    )
    mocker.patch.object(repository, "add", return_value=True)
    service = UserService(repository)
    res = service.add(user)
    repository.add.assert_called_once()
    assert res


def test_delete_user(mocker):
    repository = mocker.Mock()
    user_id = 14
    mocker.patch.object(repository, "delete", return_value=True)
    service = UserService(repository)
    res = service.delete(user_id)
    repository.delete.assert_called_once()
    assert res


def test_update_user(mocker):
    repository = mocker.Mock()
    user_old = UserDTO(
        username="timaslov",
        first_name="Тимофей",
        last_name="Маслов",
        email="timaslov@mail.ru",
    )
    user_new = UserDTO(
        username="timaslov",
        first_name="Тихон",
        last_name="Маслов",
        email="timaslov@mail.ru",
    )
    mocker.patch.object(repository, "get_by_id", return_value=user_old)
    mocker.patch.object(repository, "update", return_value=True)
    service = UserService(repository)
    res = service.update(user_new)
    repository.get_by_id.assert_called_once()
    repository.update.assert_called_once()
    assert res


def test_get_by_id_user(mocker):
    repository = mocker.Mock()
    user = UserDTO(
        username="timaslov",
        first_name="Тихон",
        last_name="Маслов",
        email="timaslov@mail.ru",
        id=7,
    )
    user_id = 7
    mocker.patch.object(repository, "get_by_id", return_value=user)
    service = UserService(repository)
    res = service.get_by_id(user_id)
    repository.get_by_id.assert_called_once()
    assert res == user


def test_get_all_users(mocker):
    repository = mocker.Mock()
    user = UserDTO(
        username="timaslov",
        first_name="Тихон",
        last_name="Маслов",
        email="timaslov@mail.ru",
        id=7,
    )
    user_list = [user]
    mocker.patch.object(repository, "get_all", return_value=user_list)
    service = UserService(repository)
    res = service.get_all()
    repository.get_all.assert_called_once()
    assert res == user_list


def test_user_login(mocker):
    repository = mocker.Mock()
    username = "timaslov"
    password = "12345"
    user = UserDTO(
        username="timaslov",
        first_name="Тихон",
        last_name="Маслов",
        email="timaslov@mail.ru",
        id=7,
    )
    mocker.patch.object(repository, "login", return_value=user)
    service = UserService(repository)
    res = service.login(username, password)
    repository.login.assert_called_once()
    assert res == user
