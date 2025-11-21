from django.urls import path,include
from . import views



app_name='testapp'

urlpatterns=[


    path('',views.IndexView.as_view(),name='index'),

    path('score_list/',views.ScoreListView.as_view(),name='score_list'),

    path('createscore/',views.ScoreCreateView.as_view(),name='createscore'),

    path('scores/<int:pk>/delete/', views.ScoreDeleteView.as_view(), name='score_delete'),

    path('search/',views.SearchScoreView.as_view(),name='searchscore'),

    path('contact/',views.ContactView.as_view(),name='contact'),

     
]