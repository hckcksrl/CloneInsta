from rest_framework.views import APIView
from rest_framework.response import Response
from . import models , serializers
from rest_framework import status


# class ListAllImages(APIView):

#     def get(self, request , format=None):
        
#         all_images = models.Image.objects.all()

#         serializer = serializers.ImageSerializer(all_images, many=True)

#         return Response(data=serializer.data)


# class ListAllComments(APIView):

#     def get(self, request , format=None):

#         all_comments = models.Comment.objects.all()

#         serializer = serializers.CommentSerializer(all_comments, many=True)

#         return Response(data=serializer.data)


# class ListAllLikes(APIView):

#     def get(self, request , format=True):
        
#         all_likes = models.Like.objects.all()

#         serializer = serializers.LikeSerializer(all_likes , many = True)

#         return Response(data = serializer.data)


class Feed(APIView):
    def get(self, request , format=None):

        user = request.user

        following_users = user.following.all()  # 해당 user를 following한 모든 user

        image_list = [] # image 모두를 저장할 배열

        for following_user in following_users :

            user_images = following_user.images.all()[:2]    # following_user 가 올린 이미지 가져온다 [:2] => 2개만

            for image in user_images:

                image_list.append(image)    # image 를 image_list에 저장

        sorted_image = sorted(image_list , 
        key = lambda image: image.creat_at , reverse=True)  # image_list를 creat_at(생성순)으로 정렬 reverse를해줘서 최신생성순으로 정렬
        # lambda 인자 : 표현식
        serializer = serializers.ImageSerializer(sorted_image, many=True)   #sorted_image를 serialize

        return Response(serializer.data)

class LikeImage(APIView):

    def get(self , request ,image_id ,format=None):

        user = request.user

        try:
            found_image = models.Image.objects.get(id = image_id)
        except models.Image.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        try:
            preexist_like = models.Like.objects.get(
                creator = user,
                image = found_image                
            )
            preexist_like.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except models.Like.DoesNotExist:
            new_like = models.Like.objects.create(
                creator = user,
                image = found_image
            )
            new_like.save()
            return Response(status=status.HTTP_200_OK)