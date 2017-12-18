from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext,loader
from .models import Choice,Question
from django.core.urlresolvers import reverse
from django.http import  Http404

# Create your views here.

def index(request):
    # return HttpResponse("Hello, world. You're at the djanho_app index.")
    # latest_question_list =  Question.objects.order_by('-pub_date')[:5]
    # output = ','.join([p.question_text for p in latest_question_list])
    # return HttpResponse(output)
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('django_app/index.html')
    # context =  RequestContext(request,{
    #     'latest_question_list':latest_question_list,
    # })
    # return  HttpResponse(template.render(context))
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #  倒序 top 5 （[:5]）
    context = {'latest_question_list': latest_question_list}
    return render(request, 'django_app/index.html', context)

def detail(request,question_id):
    # return HttpResponse("You're lookoing at question %s." % question_id)
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request,'django_app/detail.html',{'question':question})
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'django_app/detail.html',{'question': question})


def results(request,question_id):
    # response = "You're looking as the results of question %s"
    # return HttpResponse(response % question_id)
    question = get_object_or_404(Question,pk = question_id)
    return render(request,'django_app/results.html',{'question':question})

def vote(request,question_id):
    # return HttpResponse("You're voting on question %s." % question_id)
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'django_app/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('django_app:results', args=(p.id,)))













