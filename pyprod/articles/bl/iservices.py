from abc import ABC, abstractmethod

from .dto import ArticleDTO, CommentDTO


class BaseArticleService(ABC):
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
    def get_by_id(self, article_id: int) -> ArticleDTO:
        """ Получить статью по id """

    @abstractmethod
    def get_all(self) -> list[ArticleDTO]:
        """ Получить все """

    @abstractmethod
    def validate_content(self, article: ArticleDTO) -> bool:
        """ Проверить текст статьи """


class BaseCommentService(ABC):
    @abstractmethod
    def add(self, comment: CommentDTO) -> bool:
        """Добавить новый коммент"""

    @abstractmethod
    def delete(self, comment_id: int) -> bool:
        """Удалить коммент"""

    @abstractmethod
    def update(self, comment: CommentDTO) -> bool:
        """Обновить коммент"""

    @abstractmethod
    def get_by_id(self, comment_id: int) -> CommentDTO:
        """Получить коммент по id"""

    @abstractmethod
    def get_all(self) -> list[CommentDTO]:
        """ Получить все """

    @abstractmethod
    def get_all_by_article_id(self, article_id: int) -> list[CommentDTO]:
        """ Получить все комменты по id статьи"""

    @abstractmethod
    def validate_content(self, comment: CommentDTO) -> bool:
        """ Проверить текст комментария """
