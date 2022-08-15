from .models import Question, Choice

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.urls import reverse
from django.utils import timezone
from .models import Choice

from pprint import pprint as pp



class IndexView(generic.ListView):
    #model = Question
    template_name = "polls/index.html"
    #context_object_name = 'question_list'
    
    def get_queryset(self):
        """Return the last five published questions."""
        #print(f"context_object_name: {self.context_object_name}")
        #return Question.objects.order_by('-pub_date')[:5]
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
    
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())





def index_old(request):
    questions = Question.objects.order_by("pub_date")[:5]
    #...order_by("-pub_date")[:5] # "-" would make it desc
    context = {'latest_question_list':questions}
    return render(request, "polls/index.html", context)


def detail_old(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})




def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))









from django.views.generic.detail import DetailView


class ChoiceDetailView(DetailView):
    model = Choice


















from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            #return HttpResponseRedirect('/polls/your-name/')
            your_name_url = reverse("polls:your-name")
            return HttpResponseRedirect(your_name_url)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
    
    return render(request, 'name.html', {'form': form})


def your_name(request):
    if request.method == 'POST':
        print(request.POST["your_name"], type(request.POST["your_name"]))
        if request.POST["your_name"]!= None:
            the_name = request.POST["your_name"]
            return render(request, "your-name.html", {"your_name": the_name})
    
    name_url = reverse("polls:name")

    return HttpResponseRedirect(name_url)
    



