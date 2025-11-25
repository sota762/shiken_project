#djangoからpathをインポート
from django.urls import path
#views1をインポート
from . import views
#djangoからviewsをauth_viewsという別名でインポート
from django.contrib.auth import views as auth_views
#formsファイルのLoginFormクラスをインポート
from .forms import LoginForm

#アプリ名をaccounts2に指定
app_name = 'accounts2'

urlpatterns = [
    #url signupにアクセスするとSignUpViewを呼び出す
    path('signup/', views.SignUpView.as_view(), name='signup'),
    #url signup_successにアクセスするとSignUpSuccessViewを呼び出す
    path('signup_success/', views.SignUpSuccessView.as_view(), name='signup_success'),
    #url loginにアクセスするとLoginViewを呼び出す autentication_form=LoginFormでカスタムフォームを使用
    path('login/', auth_views.LoginView.as_view(template_name='login.html',authentication_form=LoginForm), name='login'),
    #url logoutにアクセスするとCustomLogoutViewを呼び出す index.htmlにリダイレクトする
    path('logout/', views.CustomLogoutView.as_view(next_page='testapp:index'), name='logout'),
    ]