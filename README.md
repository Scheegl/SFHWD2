# SFHWD2
Домашняя работа к проекту по модолю D2, команды запускаемые в shell

from news.models import *

Создать двух пользователей (с помощью метода User.objects.create_user('username')).

u1 = User.objects.create_user(username='Sasha')
u2 = User.objects.create_user(username='Petya')

Создать два объекта модели Author, связанные с пользователями.

Author.objects.create(author_user=u1)
Author.objects.create(author_user=u2)

Добавить 4 категории в модель Category.

Category.objects.create(name='Politics')
Category.objects.create(name='Business')
Category.objects.create(name='Science')
Category.objects.create(name='Health')

Добавить 2 статьи и 1 новость.

author = Author.objects.get(id=1)
Post.objects.create(author=author,category_choice='NW',title = 'Title_for_NEWS', text = 'TEXT FOR NEWS')
author = Author.objects.get(id=2)
Post.objects.create(author=author,category_choice='AR',title = 'Title_for_Article_1', text = 'TEXT FOR Article_1')
Post.objects.create(author=author,category_choice='AR',title = 'Title_for_Article_2', text = 'TEXT FOR Article_1')

Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий).

Post.objects.get(id=1).post_category.add(Category.objects.get(id=1))
Post.objects.get(id=1).post_category.add(Category.objects.get(id=2))
Post.objects.get(id=2).post_category.add(Category.objects.get(id=3))
Post.objects.get(id=2).post_category.add(Category.objects.get(id=4))
Post.objects.get(id=3).post_category.add(Category.objects.get(id=2))
Post.objects.get(id=3).post_category.add(Category.objects.get(id=3))

Создать как минимум 4 комментария к разным объектам модели Post (в каждом объекте должен быть как минимум один комментарий).

Comment.objects.create(comment_post=Post.objects.get(id=1), comment_user=Author.objects.get(id=1).author_user, text='Text_for_first_comment')
Comment.objects.create(comment_post=Post.objects.get(id=2), comment_user=Author.objects.get(id=2).author_user, text='Text_for_second_comment')
Comment.objects.create(comment_post=Post.objects.get(id=3), comment_user=Author.objects.get(id=1).author_user, text='Text_for_third_comment')
Comment.objects.create(comment_post=Post.objects.get(id=3), comment_user=Author.objects.get(id=2).author_user, text='Text_for_fourth_comment')

Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов.

Comment.objects.get(id=1).like()
Comment.objects.get(id=1).like()
Comment.objects.get(id=2).dislike()
Comment.objects.get(id=2).dislike()
Comment.objects.get(id=3).dislike()
Comment.objects.get(id=4).like()
Post.objects.get(id=1).like()
Post.objects.get(id=2).dislike()
Post.objects.get(id=3).like()


Обновить рейтинги пользователей.

author_1 = Author.objects.get(id=1)
author_1.update_rating()
author_2 = Author.objects.get(id=2)
author_2.update_rating()

Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).

best_user = Author.objects.order_by('-rating_author')[:1]
for i in best_user:
	i.rating_author 
	i.author_user.username

Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье.

best_post = Post.objects.order_by('-rating_post')[:1]
for i in best_post:
	i.time_creation
	i.author.author_user.username
	i.title
	i.preview()

Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.

all_comments = Comment.objects.all()
for i in all_comments:
	i.time_creation
	i.comment_user.username
	i.rating
	i.text
