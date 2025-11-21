from django.shortcuts import render
from django.views.generic import CreateView,TemplateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import login, get_user_model
from django.contrib.auth.views import LogoutView

CustomUser=get_user_model()

class SignUpView(CreateView):


    form_class=CustomUserCreationForm

    template_name='signup.html'

    success_url=reverse_lazy('accounts2:signup_success')

    def form_valid(self,form):



        user=form.save()
        self.object=user

        return super().form_valid(form)
    
class SignUpSuccessView(TemplateView):


    template_name='signup_success.html'



class CustomLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
