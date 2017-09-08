# coding: utf-8
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from .models import Event, Person
from .forms import CreateForm,CreateUserForm 

def index(request):
    latest_event_list = Event.objects.order_by('id')
    context = {'latest_event_list': latest_event_list}
    return render(request, 'event/index.html', context)
    
def create(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'event/create.html', {'event': event})

def create2(request):
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid(): # バリデーションを通った
            # form.cleaned_data を処理
            # ...
            e = Event(event_name=request.POST['name'], event_time=request.POST['time'], event_location=request.POST['location'], fee=request.POST['fee'], quota=request.POST['quota'])
            e.save()
            return HttpResponseRedirect('/event/') # POST 後のリダイレクト
    else:
        form = CreateForm() # 非束縛フォーム

    return render(request, 'event/contact.html', {'form': form,})
    
def create_user(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid(): # バリデーションを通った
            # form.cleaned_data を処理
            # ...
            e = Person(name=request.POST['name'])
            e.save()
            return HttpResponseRedirect('/event/') # POST 後のリダイレクト
    else:
        form = CreateUserForm() # 非束縛フォーム

    return render(request, 'event/user.html', {'form': form,})


def detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'event/detail.html', {'event': event})

def gen_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    try:
        selected_event = event.get(pk=request.POST['create'])
    except (KeyError, Event.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'event/detail.html', {
            'event': event,
            'error_message': "You didn't select a choice.",
        })
    else:
#        selected_choice.votes += 1
#        selected_choice.save()
#        # Always return an HttpResponseRedirect after successfully dealing
#        # with POST data. This prevents data from being posted twice if a
#        # user hits the Back button.
        return HttpResponseRedirect(reverse('event:create', args=(event.id,)))