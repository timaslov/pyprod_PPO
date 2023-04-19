from .iservices import BaseArticleService
from .irepository import BaseArticleRepository
from .repository import ArticleRepository
from .dto import ArticleDTO


class ArticleService(BaseArticleService):
    def __init__(self, repository: BaseArticleRepository):
        self.repository = repository

    def add(self, article: ArticleDTO) -> bool:
        """ Добавить новую статью """
        return self.repository.add(article)

    def delete(self, article: ArticleDTO) -> bool:
        """ Удалить статью """

    def update(self, article: ArticleDTO) -> bool:
        """ Обновить статью """

    def get_by_id(self, article_id: int) -> ArticleDTO:
        """ Получить статью по id """

    def get_all(self) -> list[ArticleDTO]:
        """ Получить все """

    def validate_content(self, article: ArticleDTO) -> bool:
        """ Проверить текст статьи """


def get_article_service():
    return ArticleService(ArticleRepository())
