from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # Add route depending on what the filename / article name of the markdown file is
    path("wiki/<str:article_name>", views.wiki, name="wiki"),
    # Add route for "search", which will only be really used to redirect to the "wiki" route anyways
    path("search/", views.search, name="search"),
    # Add "create_new_page" route
    path("create_new_page/", views.create_new_page, name="create_new_page"),
    # Add "random_page" route
    path("random_page/", views.random_page, name="random_page"),
    # Add "edit_page" route
    path("edit_page/<str:article_name>", views.edit_page, name="edit_page"),
]
