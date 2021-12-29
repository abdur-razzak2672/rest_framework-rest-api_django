from django.db import models


class Article(models.Model):
    article_title = models.CharField(max_length = 100)
    article_author = models.CharField(max_length = 100)
    article_email = models.CharField(max_length = 100)
    article_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.article_title
