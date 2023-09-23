from django.db import models

class User(models.Model):
    id = models.CharField(max_length= 60, primary_key=True, editable=False)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    avatar = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = ['name', 'email', 'avatar', 'created_at', 'updated_at']
    
    def __str__(self):
        return self.name
    
    @property
    def is_anonymous(self):
        return False
    
    @property
    def is_authenticated(self):
        return True
    
    class Users(models.Model):
        id = models.CharField(primary_key=True, max_length=255)
        name = models.TextField(blank=True, null=True)
        email = models.TextField(blank=True, null=True)
        avatar = models.TextField(blank=True, null=True)
        created_at = models.DateTimeField(blank=True, null=True)
        updated_at = models.DateTimeField(blank=True, null=True)

        class Meta:
            managed = False
            db_table = 'users'