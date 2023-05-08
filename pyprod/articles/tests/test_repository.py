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


@pytest.mark.django_db
def test_add_article():
    article_dto = ArticleDTO(
        title="SQL injection",
        tagline="Научитесь избегать sql-инъекций в вашем коде",
        content="Какой-то текст статьи",
        slug="sql-injection",
        status=ArticleStatus.PUBLISHED,
    )
    res = ArticleRepository().add(article_dto)
    article_count = Article.objects.count()
    assert res
    assert article_count == 1

