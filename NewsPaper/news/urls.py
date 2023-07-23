from django.urls import path
from .views import PostList, PostDetail, create_post, PostUpdate, PostDelete, subscriptions
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>', cache_page(100)(PostDetail.as_view())),
    path('create/', create_post, name='post_create'),
    path('<int:pk>/update/', PostUpdate.as_view(), name='news_update'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='news_delete'),
    path('subscriptions/', subscriptions, name='subscriptions'),
]