from django.urls import path
from . import views

app_name = "images"

urlpatterns = [
    # path(
    #     "all/",
    #     view = views.ListAllImages.as_view(),
    #     name = 'all_images'
    # ),
    # path(
    #     "comments/",
    #     view = views.ListAllComments.as_view(),
    #     name = 'all_comments'
    # ),
    # path(
    #     "likes/",
    #     view = views.ListAllLikes.as_view(),
    #     name = 'all_likes'
    # )
    path(
        "",
        view = views.Feed.as_view(),
        name = 'feed'
    ),
    path(
        "<int:image_id>/like", 
        view = views.LikeImage.as_view(),
        name = 'like_image'
    ),


]
