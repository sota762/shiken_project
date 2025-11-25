#django1のadminモジュールをインポート
from django.contrib import admin

#modelsファイルのクラスCustomUserをインポート
from .models import CustomUser

#admin.ModelAdminを継承したクラスCustomUserAdminを定義
class CustomUserAdmin(admin.ModelAdmin):


    #管理サイトで一覧表示するフィールドを指定
    list_display=('id','username')

    #管理サイトでクリック可能なリンクとして表示するフィールドを指定
    list_display_links=('id','username')


#CustomUserModelを管理サイトに登録
admin.site.register(CustomUser,CustomUserAdmin)
