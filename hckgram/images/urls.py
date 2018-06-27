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
    path(
        "<int:image_id>/unlike", 
        view = views.UnLikeImage.as_view(),
        name = 'unlike_image'
    ),
    path(
        "<int:image_id>/comments",
        view = views.CommentOnImage.as_view(),
        name = "comments"
    ),
    path(
        "comments/<int:comment_id>",
        view = views.DeleteComment.as_view(),
        name = 'delete_comments'
    ),
    path(
        "search/",
        view = views.Search.as_view(),
        name='search'
    )

]
