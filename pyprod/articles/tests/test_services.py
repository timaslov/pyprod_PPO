import datetime

from ..const import ArticleStatus
from ..dto import ArticleDTO
from ..services import ArticleService


def test_add_article(mocker):
    repository = mocker.Mock()
    article = ArticleDTO(
        title="SQL injection",
        tagline="Научитесь избегать sql-инъекций в вашем коде",
        content="Какой-то текст статьи",
        slug="sql-injection",
        status=ArticleStatus.PUBLISHED,
        parent_id=5,
        id=14,
        author_id=53,
        created_at=datetime.datetime(2022, 5, 7, 13, 26),
        updated_at=datetime.datetime(2022, 6, 9, 11, 42),
    )
    mocker.patch.object(repository, "add", return_value=True)
    service = ArticleService(repository)
    res = service.add(article)
    repository.add.assert_called_once()
    assert res


def test_delete_article(mocker):
    repository = mocker.Mock()
    article_id = 14
    mocker.patch.object(repository, "delete", return_value=True)
    service = ArticleService(repository)
    res = service.delete(article_id)
    repository.delete.assert_called_once()
    assert res


def test_update_article(mocker):
    repository = mocker.Mock()
    article_old = ArticleDTO(
        title="SQL injection",
        tagline="Научитесь избегать sql-инъекций в вашем коде",
        content="Какой-то текст статьи",
        slug="sql-injection",
        status=ArticleStatus.DRAFT,
        parent_id=5,
        id=14,
        author_id=53,
        created_at=datetime.datetime(2022, 5, 7, 13, 26),
        updated_at=datetime.datetime(2022, 6, 9, 11, 42),
    )
    article_new = ArticleDTO(
        title="SQL injection updated",
        tagline="Научитесь избегать sql-инъекций в вашем коде",
        content="Какой-то текст статьи",
        slug="sql-injection",
        status=ArticleStatus.PUBLISHED,
        parent_id=5,
        id=14,
        author_id=53,
        created_at=datetime.datetime(2022, 5, 7, 13, 26),
        updated_at=datetime.datetime(2022, 6, 9, 11, 42),
    )
    mocker.patch.object(repository, "get_by_id", return_value=article_old)
    mocker.patch.object(repository, "update", return_value=True)
    service = ArticleService(repository)
    res = service.update(article_new)
    repository.get_by_id.assert_called_once()
    repository.update.assert_called_once()
    assert res


def test_validate_article_content(mocker):
    repository = mocker.Mock()
    service = ArticleService(repository)

    valid_article = ArticleDTO(
        title="SQL injection",
        tagline="Научитесь избегать sql-инъекций в вашем коде",
        content="Какой-то текст статьи",
        slug="sql-injection",
        status=ArticleStatus.PUBLISHED,
        parent_id=5,
        id=14,
        author_id=53,
        created_at=datetime.datetime(2022, 5, 7, 13, 26),
        updated_at=datetime.datetime(2022, 6, 9, 11, 42),
    )
    assert service.validate_content(valid_article)

    invalid_article = ArticleDTO(
        title="SQL injection",
        tagline="Научитесь избегать sql-инъекций в вашем коде",
        content="Какой-то текст жопа статьи",
        slug="sql-injection",
        status=ArticleStatus.PUBLISHED,
        parent_id=5,
        id=14,
        author_id=53,
        created_at=datetime.datetime(2022, 5, 7, 13, 26),
        updated_at=datetime.datetime(2022, 6, 9, 11, 42),
    )
    assert not service.validate_content(invalid_article)
