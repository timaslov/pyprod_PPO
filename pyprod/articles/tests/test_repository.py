import pytest


from ..da import Article, Comment, ArticleRepository, CommentRepository
from ..bl import ArticleDTO, CommentDTO
from ..const import ArticleStatus


@pytest.mark.django_db
def test_delete_article():
    article_dto = ArticleDTO(
        title="SQL injection",
        tagline="Научитесь избегать sql-инъекций в вашем коде",
        content="Какой-то текст статьи",
        slug="sql-injection",
        status=ArticleStatus.PUBLISHED,
        parent_id=5,
        author_id=53,
    )
    article = Article.objects.create(
        title=article_dto.title,
        tagline=article_dto.tagline,
        content=article_dto.content,
        slug=article_dto.slug,
        status=article_dto.status,
        parent_id=article_dto.parent_id,
        author_id=article_dto.author_id,
    )
    res = ArticleRepository().delete(article.id)
    article_count = Article.objects.count()
    assert res
    assert article_count == 0


# @pytest.mark.django_db
# def test_get_user_by_id():
#     user_dto = UserDTO(
#         username="timaslov",
#         first_name="Тихон",
#         last_name="Маслов",
#         email="timaslov@mail.ru",
#         password="12345",
#     )
#     user = User.objects.create_user(
#         username=user_dto.username,
#         first_name=user_dto.first_name,
#         last_name=user_dto.last_name,
#         email=user_dto.email,
#         password=user_dto.password,
#     )
#     res = UserRepository().get_by_id(user.id)
#     assert user_dto.username == res.username
#     assert user_dto.first_name == res.first_name
#     assert user_dto.last_name == res.last_name
#     assert user_dto.email == res.email
