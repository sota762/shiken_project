#django.dbからmodelsをインポート
from django.db import models

#djangoからAbstractUserをインポート
from django.contrib.auth.models import AbstractUser

#AbstractUserを継承したクラスCustomUserを定義
class CustomUser(AbstractUser):


    pass
