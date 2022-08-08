from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    
    
    # ex: /polls/
    path("", views.QuestionIndexView.as_view(), name="index"),
    
    
    # ex: /polls/old/
    path('old/', views.index_old, name='index_old'),
    # ex: /polls/old/5/
    path('old/<int:question_id>/', views.detail_old, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]




print(urlpatterns[0].name)
print(f"name is: {urlpatterns[0].name}")

