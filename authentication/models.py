from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from PIL import Image
from django.utils import timezone
from gdstorage.storage import GoogleDriveStorage
import os



"""
from gdstorage.storage import GoogleDriveStorage, GoogleDrivePermissionType, GoogleDrivePermissionRole, GoogleDriveFilePermission

permission =  GoogleDriveFilePermission(
   GoogleDrivePermissionRole.READER,
   GoogleDrivePermissionType.USER,
   "foo@mailinator.com"
)

gd_storage = GoogleDriveStorage(permissions=(permission, ))
"""

class User(AbstractUser):
    
    souscris = models.BooleanField(default=False)
    date_birth = models.DateField(verbose_name = "date de naissance",null=True, blank=True)
    place_birth = models.CharField(max_length=128, verbose_name="lieu de naissance")
    profession = models.CharField(max_length=128)
    lieu = models.CharField(max_length=128)
    diplome = models.CharField(max_length=128, verbose_name='Dernier diplome')
    description = models.TextField(max_length=256)
    date_edit = models.DateTimeField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def storage():
        storage = None
        if os.environ.get('ENV') == 'PRODUCTION':
            gd_storage = GoogleDriveStorage()
            storage = gd_storage
        return storage
    
    profile_photo = models.ImageField(verbose_name='photo de profil', null=True, blank=True, storage=storage())




    """
    IMAGE_MAX_SIZE = (800, 800)

    def resize_image(self):
        if self.profile_photo.path:
            print('no')
        else:
            print("yes")
            profile_photo = Image.open(self.profile_photo)
            profile_photo.thumbnail(self.IMAGE_MAX_SIZE)
            profile_photo.save(self.profile_photo.path)



   
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.resize_image()
    """
    def save(self, *args, **kwargs):
        self.date_edit = timezone.now()
        super().save(*args, **kwargs)
        #self.resize_image()