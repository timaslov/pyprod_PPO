import datetime

from ..const import ArticleStatus
from ..dto import ArticleDTO, CommentDTO
from ..services import ArticleService, CommentService


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


def test_get_by_id_article(mocker):
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
    article_id = 14
    mocker.patch.object(repository, "get_by_id", return_value=article)
    service = ArticleService(repository)
    res = service.get_by_id(article_id)
    repository.get_by_id.assert_called_once()
    assert res == article


def test_get_all_article(mocker):
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
    article_list: list[ArticleDTO] = [article]
    mocker.patch.object(repository, "get_all", return_value=article_list)
    service = ArticleService(repository)
    res = service.get_all()
    repository.get_all.assert_called_once()
    assert res == article_list


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
        content="Какой-то текст ban_word1 статьи",
        slug="sql-injection",
        status=ArticleStatus.PUBLISHED,
        parent_id=5,
        id=14,
        author_id=53,
        created_at=datetime.datetime(2022, 5, 7, 13, 26),
        updated_at=datetime.datetime(2022, 6, 9, 11, 42),
    )
    assert not service.validate_content(invalid_article)


def test_add_comment(mocker):
    repository = mocker.Mock()
    comment = CommentDTO(
        content="Отличная статья",
        article_id=5,
        id=7,
        author_id=3,
        created_at=datetime.datetime(2022, 5, 7, 13, 26)
    )
    mocker.patch.object(repository, "add", return_value=True)
    service = CommentService(repository)
    res = service.add(comment)
    repository.add.assert_called_once()
    assert res


def test_delete_comment(mocker):
    repository = mocker.Mock()
    comment_id = 14
    mocker.patch.object(repository, "delete", return_value=True)
    service = CommentService(repository)
    res = service.delete(comment_id)
    repository.delete.assert_called_once()
    assert res


def test_update_comment(mocker):
    repository = mocker.Mock()
    comment_old = CommentDTO(
        content="Отличная статья",
        article_id=5,
        id=7,
        author_id=3,
        created_at=datetime.datetime(2022, 5, 7, 13, 26)
    )
    comment_new = CommentDTO(
        content="Плохая статья",
        article_id=5,
        id=7,
        author_id=3,
        created_at=datetime.datetime(2022, 6, 7, 14, 26)
    )
    mocker.patch.object(repository, "get_by_id", return_value=comment_old)
    mocker.patch.object(repository, "update", return_value=True)
    service = CommentService(repository)
    res = service.update(comment_new)
    repository.get_by_id.assert_called_once()
    repository.update.assert_called_once()
    assert res


def test_get_by_id_comment(mocker):
    repository = mocker.Mock()
    comment = CommentDTO(
        content="Отличная статья",
        article_id=5,
        id=7,
        author_id=3,
        created_at=datetime.datetime(2022, 5, 7, 13, 26)
    )
    comment_id = 7
    mocker.patch.object(repository, "get_by_id", return_value=comment)
    service = CommentService(repository)
    res = service.get_by_id(comment_id)
    repository.get_by_id.assert_called_once()
    assert res == comment


def test_get_all_comment(mocker):
    repository = mocker.Mock()
    comment = CommentDTO(
        content="Отличная статья",
        article_id=5,
        id=7,
        author_id=3,
        created_at=datetime.datetime(2022, 5, 7, 13, 26)
    )
    comment_list: list[CommentDTO] = [comment]
    mocker.patch.object(repository, "get_all", return_value=comment_list)
    service = CommentService(repository)
    res = service.get_all()
    repository.get_all.assert_called_once()
    assert res == comment_list


def test_get_all_by_article_id_comment(mocker):
    repository = mocker.Mock()
    comment = CommentDTO(
        content="Отличная статья",
        article_id=5,
        id=7,
        author_id=3,
        created_at=datetime.datetime(2022, 5, 7, 13, 26)
    )
    comment_list: list[CommentDTO] = [comment]
    mocker.patch.object(repository, "get_all_by_article_id", return_value=comment_list)
    service = CommentService(repository)
    res = service.get_all_by_article_id(7)
    repository.get_all_by_article_id.assert_called_once()
    assert res == comment_list

