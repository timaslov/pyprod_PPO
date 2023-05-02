from .iservices import BaseArticleService
from .irepository import BaseArticleRepository
from .repository import ArticleRepository
from .dto import ArticleDTO


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
        with open("articles/banned_words.txt", "r") as file:
            for line in file:
                word = line.strip()
                if word in article.content:
                    return False

        return True


def get_article_service():
    return ArticleService(ArticleRepository())
