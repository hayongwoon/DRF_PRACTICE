from blog.models import Article, Category

# 게시글 작성 함수
def create_an_article(title, user_id, category, content):
    article = Article(title=title, user=user_id, content=content)
    article.save()
    category = Category.objects.get(name=category)
    article.category.add(category)
    return article  