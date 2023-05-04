from .iservices import BaseArticleService, BaseCommentService
from .irepository import BaseArticleRepository, BaseCommentRepository
from .dto import ArticleDTO, CommentDTO
from ..text_validators import validate_text


class ArticleService(BaseArticleService):
    def __init__(self, repository: BaseArticleRepository):
        self.repository = repository

    def add(self, article: ArticleDTO) -> bool:
        if not self.validate_content(article):
            return False

        return self.repository.add(article)

    def delete(self, article_id: int) -> bool:
        if not self.get_by_id(article_id):
            return False
        return self.repository.delete(article_id)

    def update(self, article: ArticleDTO) -> bool:
        if not self.get_by_id(article.id) or not self.validate_content(article):
            return False
        return self.repository.update(article)

    def get_by_id(self, article_id: int) -> ArticleDTO:
        return self.repository.get_by_id(article_id)

    def get_all(self) -> list[ArticleDTO]:
        return self.repository.get_all()

    def validate_content(self, article: ArticleDTO) -> bool:
        return validate_text(article.content)


class CommentService(BaseCommentService):
    def __init__(self, repository: BaseCommentRepository):
        self.repository = repository

    def add(self, comment: CommentDTO) -> bool:
        if not self.validate_content(comment):
            return False
        return self.repository.add(comment)

    def delete(self, comment_id: int) -> bool:
        if not self.get_by_id(comment_id):
            return False
        return self.repository.delete(comment_id)

    def update(self, comment: CommentDTO) -> bool:
        if not self.get_by_id(comment.id) or not self.validate_content(comment):
            return False
        return self.repository.update(comment)

    def get_by_id(self, comment_id: int) -> CommentDTO:
        return self.repository.get_by_id(comment_id)

    def get_all(self) -> list[CommentDTO]:
        return self.repository.get_all()

    def get_all_by_article_id(self, article_id: int) -> list[CommentDTO]:
        return self.repository.get_all_by_article_id(article_id)

    def validate_content(self, comment: CommentDTO) -> bool:
        return validate_text(comment.text)
