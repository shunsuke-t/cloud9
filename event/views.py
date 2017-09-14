# coding: utf-8
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from .models import Event, Person
from .forms import CreateForm,CreateUserForm, EventForm, SelectUserForm

def index(request):
    latest_event_list = Event.objects.order_by('id')
    member_list = Person.objects.order_by('id')
    form = SelectUserForm()
    context = {
        'latest_event_list': latest_event_list,
        'member_list': member_list,
        'form': form
    }
    return render(request, 'event/index.html', context)
    
def create(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'event/create.html', {'event': event})

def create2(request):
    #Event = get_object_or_404(Event, Event.id)
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid(): # バリデーションを通った
            # form.cleaned_data を処理
            # ...
            e = Event(
                author=request.POST['author'],
                event_name=request.POST['event_name'], 
                event_image=request.POST['event_image'], 
                event_datetime=request.POST['event_datetime'], 
                event_location=request.POST['event_location'], 
                num_of_members=request.POST['num_of_members'], 
                dead_line=request.POST['dead_line'],
                overview=request.POST['overview']
            )
            e.save()
            return HttpResponseRedirect('/event/') # POST 後のリダイレクト
    else:
        form = CreateForm() # 非束縛フォーム

    return render(request, 'event/contact.html', {'form': form,})

def edit(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid(): # バリデーションを通った
            form.save()
            return HttpResponseRedirect('/event/') # POST 後のリダイレクト
    else:
        form = EventForm(instance=event) # 非束縛フォーム

    edit_context = {'form': form, 'event':event}
    return render(request, 'event/edit.html', context=edit_context)
    
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
    
    return render(request, 'event/edit.html', {'form': form,})


def detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    memberslist = event.members.all()
    context = {
        'event': event,
        'memberslist':memberslist
    }
    return render(request, 'event/detail.html', context)

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

def event_join(request, event_id):
    target_event = get_object_or_404(Event, id=event_id)
    new_member = get_object_or_404(Person, id=request.POST['new_members'],)
    target_event.members.add(new_member)
    return HttpResponseRedirect('/event/')