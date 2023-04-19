from dataclasses import asdict

from .irepository import BaseArticleRepository
from .dto import ArticleDTO
from .models import Article


class ArticleRepository(BaseArticleRepository):
    def add(self, article: ArticleDTO) -> bool:
        return Article.objects.create(**asdict(article))

    def delete(self, article: ArticleDTO) -> bool:
        """ Удалить статью """

    def update(self, article: ArticleDTO) -> bool:
        """ Обновить статью """

    def get_by_id(self, article_id: int) -> ArticleDTO | None:
        return Article.objects.filter(pk=article_id).first()

    def get_all(self) -> list[ArticleDTO]:
        """ Получить все """
