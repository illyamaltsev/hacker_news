from django.db import models


# - Create CRUD API to manage news posts.
#   The post will have the next fields: title, link, creation date, amount of upvotes, author-name
# - Posts should have CRUD API to manage comments on them.
#   The comment will have the next fields: author-name, content, creation date

class Post(models.Model):
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    author_name = models.CharField(max_length=200)

    up_votes_amount = models.IntegerField()

    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('hn_rest_api.Post', on_delete=models.CASCADE, related_name='comments')
    author_name = models.CharField(max_length=200)
    content = models.TextField()

    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
