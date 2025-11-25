#djangoのユーザー作成フォーム(UserCreateForm)と認証フォーム(AuthenticationForm)をインポート
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
#djangoのget_user_modelをインポート
from django.contrib.auth import get_user_model

#プロジェクトで使われているユーザーモデルをCustomUserという名前で取得
CustomUser=get_user_model()

#UserCreationFormを継承したクラスCustomUserCreationFormを定義
class CustomUserCreationForm(UserCreationForm):
    #内部クラスMetaを定義
    class Meta:


        #このフォームが操作するモデルをCustomUserに指定
        model=CustomUser

        #フォームで使用するフィールドを指定
        fields=('username','email','password1','password2')

#AuthenticationFormを継承したクラスLoginを定義
class LoginForm(AuthenticationForm):
    #内部クラスMetaを定義
    class Meta:

        #このフォームが操作するモデルをCustomUserに指定
        model=CustomUser

        #フォームで使用するフィールドを指定
        fields=['username','password']