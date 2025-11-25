#djangoからrenderをインポート
from django.shortcuts import render
#djangoから汎用クラスベースビューをインポート
from django.views.generic import CreateView,TemplateView
#formsファイルからCustomUserCreationFormをインポート
from .forms import CustomUserCreationForm
#djangoからreverse_lazyをインポート
from django.urls import reverse_lazy
#djangoからloginとget_user?modelをインポート
from django.contrib.auth import login, get_user_model
#djangoからLogoutViewクラスをインポート
from django.contrib.auth.views import LogoutView

#現在のプロジェクトで使われているユーザーモデルを取得し,CustomUserに代入
CustomUser=get_user_model()

#CreateViewを継承したクラスSignUpViewを定義
class SignUpView(CreateView):

    #使用するフォームをCustomUserCreationFormに指定
    form_class=CustomUserCreationForm

    #signup.htmlをレンダリング
    template_name='signup.html'

    #フォーム送信が成功したときにリダイレクトするURLをsignup_successに指定
    success_url=reverse_lazy('accounts2:signup_success')

    #フォームが有効な場合に呼び出されるメソッドをオーバーライド
    def form_valid(self,form):



        #フォームデータを保存してuserオブジェクトを生成
        user=form.save()
        self.object=user

        #親クラスのform_validを呼び出しリダイレクト処理を実行する
        return super().form_valid(form)
    
#TemplateViewを継承したクラスSignUpSuccessViewを定義
class SignUpSuccessView(TemplateView):


    #signup_success.htmlをレンダリング
    template_name='signup_success.html'


#LogoutViewを継承したクラスCustomLogoutViewを定義
class CustomLogoutView(LogoutView):
    #GETリクエストでもログアウトできるように設定
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
