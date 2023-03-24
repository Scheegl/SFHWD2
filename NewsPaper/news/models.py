from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


class Author(models.Model):
    author_user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating_author = models.IntegerField(default=0)

    def update_rating(self):
        author_rait = self.post_set.aggregate(postRating=Sum('rating_post'))
        author_r = 0
        author_r += author_rait.get('postRating')

        comment_rait = self.author_user.comment_set.aggregate(comment_rating=Sum('rating'))
        comment_r = 0
        comment_r += comment_rait.get('comment_rating')

        self.rating_author = author_r *3 + comment_r
        self.save()


class Category(models.Model):
    category_name = models.CharField(max_length=32, unique=True)

    #def __str__(self):
        #return self.category_name()


class Post(models.Model):
    author = models.ForeignKey("Author", on_delete=models.CASCADE)

    NEWS = 'NW'
    ARTICLE = "AR"
    CATEGORY_CHOICES = (
        (NEWS, 'Новость'),
        (ARTICLE, 'Статья')
    )
    category_choice = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=ARTICLE)
    time_creation = models.DateTimeField(auto_now_add=True)
    post_category = models.ManyToManyField(Category, through="PostCategory")
    title = models.CharField(max_length=64, unique=True)
    text = models.TextField()
    rating_post = models.IntegerField(default=0)


    def like(self):
        self.rating_post +=1
        self.save()

    def dislike(self):
        self.rating_post -=1
        self.save()

    def preview(self):
        return self.text[0:123] + '...'

    def __str__(self):
        return f'{self.title()}: {self.text[:20]}'


class PostCategory(models.Model):
    _post = models.ForeignKey("Post", on_delete=models.CASCADE)
    _category = models.ForeignKey("Category", on_delete=models.CASCADE)


class Comment(models.Model):
    comment_post = models.ForeignKey("Post", on_delete=models.CASCADE)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=1024)
    time_creation = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating +=1
        self.save()

    def dislike(self):
        self.rating -=1
        self.save()