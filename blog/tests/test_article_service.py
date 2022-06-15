from django.test import TestCase
from blog.models import Category
from user.models import User

from blog.services.article_service import (
    create_an_article
)


class TestArticleService(TestCase):
    def test_you_can_create_an_article(self):
        # Given
        title = "test_title"
        user = User.objects.create_user(username='testname')
        category = Category.objects.create(name='QnA')
        content = 'test_content'

        # When
        article = create_an_article(title, user, category, content)

        # Then
        self.assertEqual(article.title, title)

    