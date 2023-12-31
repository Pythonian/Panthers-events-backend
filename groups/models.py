from django.db import models
from users.models import Users
from events.models import Events, Images
import uuid

def genUUID():
    return str(uuid.uuid4())

class Groups(models.Model):
    id = models.CharField(primary_key=True, max_length=255, default=genUUID)
    title = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    class Meta:
        managed = False
        db_table = 'groups'


class UserGroups(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE)
    group = models.ForeignKey(Groups, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'user_groups'
        # unique_together = (('user', 'group'),)


class GroupEvents(models.Model):
    event = models.OneToOneField(Events, on_delete=models.CASCADE)
    group = models.ForeignKey(Groups, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'group_events'
        # unique_together = (('group', 'event'),)


class GroupImage(models.Model):
    group = models.OneToOneField(Groups, on_delete=models.CASCADE)
    image = models.ForeignKey(Images, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'group_image'
        unique_together = (('group', 'image'),)
