from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    
    
    # ex: /polls/
    path("", views.IndexView.as_view(), name="index"),
    # ex: /polls/5/
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    # ex: /polls/5/results/
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),


    # ex: /polls/old/
    path('old/', views.index_old, name='index_old'),
    # ex: /polls/old/5/
    path('old/<int:question_id>/', views.detail_old, name='detail_old'),
    # ex: /polls/old/5/results/
    path('old/<int:question_id>/results/', views.results, name='results_old'),
    

]




print(urlpatterns[0].name)
print(f"name is: {urlpatterns[0].name}")

