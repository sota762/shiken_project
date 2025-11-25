from django.shortcuts import render

from django.views.generic import TemplateView,ListView,CreateView,DeleteView,FormView

from .models import ScoreCategory

from .forms import ScoreCategoryForm

from django.urls import reverse_lazy

from django.db.models import Q

from .forms import ContactForm

from django.contrib import messages

from django.core.mail import EmailMessage

from django.contrib.auth.mixins import LoginRequiredMixin





class IndexView(TemplateView):


    template_name='index.html'


class ScoreListView(LoginRequiredMixin,ListView):

    login_url='/accounts2/login/'

    model=ScoreCategory

    template_name='score_list.html'

    context_object_name='scores'

    def get_queryset(self):

        queryset=ScoreCategory.objects.filter(user=self.request.user).order_by('-posted_at')

        query=self.request.GET.get('q')

        if query:
            try:
                score_value=int(query)
                queryset=queryset.filter(
                    Q(score=score_value)
            )
            except ValueError:
                pass

        selected_category=self.request.GET.get('category')
        if selected_category:
            queryset=queryset.filter(category=selected_category)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ScoreCategory.CATEGORY  # プルダウン用科目リスト
        selected_category=self.request.GET.get('category', '')
        context['selected_category']=selected_category

        category_jp=dict(ScoreCategory.CATEGORY)
        context['selected_category_label']=category_jp.get(selected_category,"すべての科目")
        return context
    
class ScoreCreateView(LoginRequiredMixin,CreateView):

    login_url='/accounts2/login/'
    template_name='createscore.html'
    model=ScoreCategory
    form_class=ScoreCategoryForm
    success_url=reverse_lazy('testapp:score_list')

    def form_valid(self, form):
        
        form.instance.user=self.request.user

        return super().form_valid(form)
    
class ScoreDeleteView(DeleteView):


    model=ScoreCategory

    template_name=None

    success_url=reverse_lazy('testapp:score_list')

    def get_queryset(self):
        return ScoreCategory.objects.filter(user=self.request.user)
    
class SearchScoreView(ListView):
    model=ScoreCategory
    template_name='score_list.html'
    context_object_name='searchscore'


class ContactView(FormView):
    '''問い合わせページを表示するビュー

    フォームで入力されたデータを取得し、メールの作成と送信を行う
    '''
    #conatct.htmlをレンダリングする
    template_name='contact.html'
    #クラス変数form_classにforms.pyで定義したContactFormを設定
    form_class=ContactForm

    success_url=reverse_lazy('testapp:contact')

    def form_valid(self, form):
        '''FormViewクラスのform_vaildをオーバーライド

        フォームのバリデーションを通過したデータがＰＯＳＴされたときに呼ばれる
        メール送信を行う

        parameters:
            form(object): ContactFormのオブジェクト
        Return:
            HttpResponseRedirectのオブジェクト
            オブジェクトをインスタンス化するとsuccess_urlで
            設定されているＵＲＬにリダイレクトされる
        '''
        name=form.cleaned_data['name']
        email=form.cleaned_data['email']
        title=form.cleaned_data['title']
        message=form.cleaned_data['message']

        subject='お問い合わせ:{}'.format(title)

        message=\
            '送信者名:{0}\nメールアドレス:{1}\n タイトル:{2}\n メッセージ:\n{3}'\
            .format(name,email,title,message)
        
        from_email='kmm2559303@stu.o-hara.ac.jp'

        to_list=['kmm2559303@stu.o-hara.ac.jp']

        message=EmailMessage(subject=subject,
                             body=message,
                             from_email=from_email,
                             to=to_list,
                             )
        
        message.send()

        messages.success(
            self.request, 'お問い合わせは正常に送信されました。')
        
        return super().form_valid(form)

    
    


