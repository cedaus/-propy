from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Question, Choice

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-publish_date')[:5]
    return render(request, 'polls/index.html', {'latest_question_list': latest_question_list})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        try:
            selected_choice = question.choice_set.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
            return render(request, 'polls/detail.html', {'question': question, 'error_message': "You didn't select a choice.",})
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('results', args=(question.id,)))
    else:
        return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
