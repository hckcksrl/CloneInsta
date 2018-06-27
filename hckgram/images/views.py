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

    def post(self , request ,image_id ,format=None):

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
            return Response(status=status.HTTP_304_NOT_MODIFIED)
        except models.Like.DoesNotExist:
            new_like = models.Like.objects.create(
                creator = user,
                image = found_image
            )
            new_like.save()
            return Response(status=status.HTTP_200_OK)


class UnLikeImage(APIView):

    def delete(self,request,image_id,format=None):

        user = request.user

        try:
            found_image = models.Image.objects.get(id = image_id)
        except models.Image.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        try:
            exist_like = models.Like.objects.get(
                creator= user,
                image = found_image
            )
            exist_like.delete()
            return Response(status =status.HTTP_204_NO_CONTENT)

        except models.Like.DoesNotExist:
            return Response(status=status.HTTP_304_NOT_MODIFIED)



class CommentOnImage(APIView):

    def post(self,request,image_id,format=None):

        user = request.user

        try:
            found_image = models.Image.objects.get(id = image_id)   # comment 달려고하는 image가 있는지 확인
        except models.Image.DoesNotExist :
            return Response(status =status.HTTP_404_NOT_FOUND)

        serializer = serializers.CommentSerializer(data = request.data) #  data를 serializer한다.(CommentSerializer)형태

        if serializer.is_valid() :  #   serializer 가 있으면
            serializer.save(creator=user, image = found_image)  #   serializer save를한다. creator 는 user , image 는 found_image
            return Response(data = serializer.data , status=status.HTTP_201_CREATED)
        else : 
            return Response(data = serializer.errors,status = status.HTTP_400_BAD_REQUEST)

class DeleteComment(APIView):

    def delete(self,request,comment_id,format =None):
        
        user = request.user

        try:
            found_comment = models.Comment.objects.get(id = comment_id , creator = user)    
            #   삭제할려는 comment의  comment_id를 찾고    찾은 comment의 creator 가 user와 같으면
            found_comment.delete()  #   found_comment 를 삭제
            return Response(status=status.HTTP_200_OK)
        except models.Comment.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        

class Search(APIView):

    def get(self , request, format=None):

        hashtags = request.query_params.get('hashtags',None)
        
        if hashtags is not None:
            hashtags = hashtags.split(",")
            
            images = models.Image.objects.filter(
                tags__name__in = hashtags).distinct() 
            #   tags__name__in 은  Deep Relationship이다
            #   A__B__contains,exact 는 객체안의 A객체 안의 B의 값이 contains, exact 일떄 대소문자 구별 은 앞에 i를 붙이면됨
            
            serializer = serializers.CountImageSerializer(images , many=True)

            return Response(data = serializer.data , status = status.HTTP_200_OK)

        else :
            return Response(status = status.HTTP_400_BAD_REQUEST)