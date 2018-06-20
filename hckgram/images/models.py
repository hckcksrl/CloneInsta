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

class Comment(TimeStampModel):

    message = models.TextField()
    image = models.ForeignKey(Image,on_delete = models.CASCADE, null=True)
    creator = models.ForeignKey(user_models.User,on_delete = models.CASCADE,null=True)

class Like(TimeStampModel):

    creator = models.ForeignKey(user_models.User,on_delete = models.CASCADE, null=True)
    image = models.ForeignKey(Image,on_delete = models.CASCADE, null=True)