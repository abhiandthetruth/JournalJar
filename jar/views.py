from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import TopicForm, EntryForm
from .models import Topic,Entry

# Create your views here.
def index(request):
    return render(request, 'jar/index.html')

def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics' : topics}
    return render(request, 'jar/topics.html', context)

def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    print(topic)
    #minus for reverse order
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'jar/topic.html', context)

def new_topic(request):
    if request.method != 'POST':
        #form not processed
        form = TopicForm()
    else:
        #form processed
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('jar:topics'))
    context = {'form': form}
    return render(request, 'jar/new_topic.html', context)

def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('jar:topic', args=(topic_id,)))
    context = {'topic':topic, 'form':form}
    return render(request, 'jar/new_entry.html', context)

def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('jar:topic', 
                args=(topic.id,)))
    context = {'form':form, 'entry':entry, 'topic':topic}
    return render(request, 'jar/edit_entry.html', context)
