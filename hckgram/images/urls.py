from django.urls import path
from . import views

app_name = "images"

urlpatterns = [
    path(
        "",
        view = views.Images.as_view(),
        name = 'feed'
    ),
    path(
        "<int:image_id>",
        view = views.ImageDetail.as_view(),
        name = 'image_detail'
    ),
    path(
        "<int:image_id>/likes", 
        view = views.LikeImage.as_view(),
        name = 'like_image'
    ),
    path(
        "<int:image_id>/unlikes", 
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
    ),
    path(
        "<int:image_id>/comments/<int:comment_id>",
        view = views.ImageComment.as_view(),
        name = 'image_comment_delete'
    )

]
