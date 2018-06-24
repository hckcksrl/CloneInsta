from django.db import models
from hckgram.users import models as user_models
# Create your models here.
class TimeStampModel(models.Model):
   
    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True



class Image(TimeStampModel):

    file = models.ImageField()
    location = models.CharField(max_length=140)
    caption = models.TextField()
    creator = models.ForeignKey(user_models.User,on_delete = models.CASCADE, null=True)


    def __str__(self):
        return '{} - {}'.format(self.location,self.caption)

class Comment(TimeStampModel):

    message = models.TextField()
    image = models.ForeignKey(Image,on_delete = models.CASCADE, null=True, related_name = 'comments')
    creator = models.ForeignKey(user_models.User,on_delete = models.CASCADE,null=True)

    def __str__(self):
        return self.message

class Like(TimeStampModel):

    creator = models.ForeignKey(user_models.User,on_delete = models.CASCADE, null=True)
    image = models.ForeignKey(Image,on_delete = models.CASCADE, null=True , related_name = 'likes')

    def __str__(self):
        return 'User: {} - Image Caption: {}'.format(self.creator.username , self.image.caption)