from django.urls import path

from . import views
from . import error_handlers
from django.conf.urls import (
handler400, handler403, handler404, handler500
)
from . import forms

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
    path('form/', forms.form_view, name='form'),
    
    
    path('article/<int:pk>/', views.ChoiceDetailView.as_view()),
    path('name/', views.get_name, name = "name"),
    path('your-name/', views.your_name, name = "your-name"),

    # ex: /polls/old/
    path('old/', views.index_old, name='index_old'),
    # ex: /polls/old/5/
    path('old/<int:question_id>/', views.detail_old, name='detail_old'),
    # ex: /polls/old/5/results/
    path('old/<int:question_id>/results/', views.results, name='results_old'),
    

]



handler404 = error_handlers.my_custom_not_found



#print(urlpatterns[0].name)
#print(f"name is: {urlpatterns[0].name}")

