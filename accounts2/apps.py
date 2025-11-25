#djangoのappsからAppConfigをインポート
from django.apps import AppConfig

#AppConfigを継承したクラスAccouonts2Configを定義
class Accounts2Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts2'
