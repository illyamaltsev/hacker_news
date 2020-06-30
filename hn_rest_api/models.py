from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField(max_length=200)
    author_name = models.CharField(max_length=200)

    up_votes_amount = models.IntegerField(default=0)

    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        "hn_rest_api.Post", on_delete=models.CASCADE, related_name="comments"
    )

    author_name = models.CharField(max_length=200)
    content = models.TextField()

    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
