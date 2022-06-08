from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.
class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """
    Database model for users in the system
    """

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    # tasks = models.ManyToManyField('Task', blank=True)
    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """
        Retrieves full name of user
        """
        return self.name
    
    def get_short_name(self):
        """
        Retrieves short name of user
        """
        return self.name
    
    def __str__(self):
        """
        Returns string representation of our user
        """
        return self.email

# class Task(models.Model):
#     """
#     Database model for tasks in the system
#     """
#     user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
#     task_name = models.CharField(max_length=255)
#     task_description = models.TextField()
#     task_completed = models.BooleanField(default=False)
#     task_created = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         """
#         Returns string representation of our task
#         """
#         return self.task_name