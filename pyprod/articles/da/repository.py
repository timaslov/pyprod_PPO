from dataclasses import asdict

from ..bl import BaseArticleRepository, BaseCommentRepository, ArticleDTO, CommentDTO
from .models import Article, Comment


class ArticleRepository(BaseArticleRepository):
    def add(self, article: ArticleDTO) -> bool:
        return Article.objects.create(**asdict(article))

    def delete(self, article_id: int) -> bool:
        return Article.objects.filter(pk=article_id).delete()

    def update(self, article: ArticleDTO) -> bool:
        return Article.objects.filter(pk=article.id).update(**asdict(article))

    def get_by_id(self, article_id: int) -> ArticleDTO | None:
        return Article.objects.filter(pk=article_id).first()

    def get_all(self) -> list[ArticleDTO]:
        return Article.objects.all()


class CommentRepository(BaseCommentRepository):
    def add(self, comment: CommentDTO) -> bool:
        return Comment.objects.create(**asdict(comment))

    def delete(self, comment_id: int) -> bool:
        return Comment.objects.filter(pk=comment_id).delete()

    def update(self, comment: CommentDTO) -> bool:
        return Comment.objects.filter(pk=comment.id).update(**asdict(comment))

    def get_by_id(self, comment_id: int) -> CommentDTO | None:
        return Comment.objects.filter(pk=comment_id).first()

    def get_all(self) -> list[CommentDTO]:
        return Comment.objects.all()

    def get_all_by_article_id(self, article_id: int) -> list[CommentDTO]:
        return Comment.objects.filter(article_id=article_id)
