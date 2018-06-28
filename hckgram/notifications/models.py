from django.db import models
from hckgram.users import models as user_models
from hckgram.images import models as images_models

class Notification(images_models.TimeStampModel):

    TYPE_CHOICES = (
        ('like','Like'),
        ('comment','Comment'),
        ('follow','Follow')
    )

    creator = models.ForeignKey(user_models.User,
    on_delete = models.CASCADE,related_name = 'creator')

    to = models.ForeignKey(user_models.User,
    on_delete = models.CASCADE,related_name='to')
    
    notification_type = models.CharField(max_length=20,choices = TYPE_CHOICES)
    
    image = models.ForeignKey(images_models.Image,
    on_delete = models.CASCADE)
    comment = models.TextField(null = True , blank= True)

    class Meta :
        ordering = ['-creat_at']

    def __str__(self):
        return 'From : {} - {}'.format(self.creator,self.to)