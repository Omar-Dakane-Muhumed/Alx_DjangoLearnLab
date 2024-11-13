from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
        # New field: Date of birth
        date_of_birth = models.DateField(null=True, blank=True)
        
        # New field: Profile photo
        profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

        def _str_(self):
            return self.username



from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, date_of_birth=None, profile_photo=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, date_of_birth=date_of_birth, profile_photo=profile_photo, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, date_of_birth=None, profile_photo=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, password, date_of_birth, profile_photo, **extra_fields)


from django.db import models

class Book(models.Model):
    # Model fields
    name = models.CharField(max_length=255)

    class Meta:
        permissions = [
            ("can_view", "Can view model"),
            ("can_create", "Can create model"),
            ("can_edit", "Can edit model"),
            ("can_delete", "Can delete model"),
        ]
