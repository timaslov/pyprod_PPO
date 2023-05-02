from abc import ABC, abstractmethod

from .dto import ArticleDTO


class BaseArticleRepository(ABC):
    @abstractmethod
    def add(self, article: ArticleDTO) -> bool:
        """ Добавить новую статью """

    @abstractmethod
    def delete(self, article_id: int) -> bool:
        """ Удалить статью """

    @abstractmethod
    def update(self, article: ArticleDTO) -> bool:
        """ Обновить статью """

    @abstractmethod
    def get_by_id(self, article_id: int) -> ArticleDTO | None:
        """ Получить статью по id """

    @abstractmethod
    def get_all(self) -> list[ArticleDTO]:
        """ Получить все """
