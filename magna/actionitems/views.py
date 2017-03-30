from django.http import HttpResponse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User

from django.shortcuts import render
from .models import Issue, Line
from django.urls import reverse
from .forms import IssueForm, SearchForm

def index(request):
    line_list = Line.objects.order_by('-name')
    context = {'line_list': line_list}
    return render(request, 'actionitems/index.html', context )

def search(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            field = data['team']
            #team = User.objects.get(id=field)
            item_list = Issue.objects.filter(team=field.id)
            context = {'item_list': item_list, 'form': form}
            return render(request, 'actionitems/search.html',context, { 'form': form})
    else:
        form = SearchForm()

        return render(request, 'actionitems/search.html',{ 'form': form})

def detail(request, line_id):
    item_list = Issue.objects.filter(lineid=line_id).order_by('-openDate')
    context = {'item_list': item_list, 'line_id': line_id}
    return render(request, 'actionitems/detail.html', context)

def new(request, line_id):
    if request.method == "POST":
        form = IssueForm(request.POST)
        actionItem = form.save(commit = False)
        actionItem.save()
        item_list = Issue.objects.filter(lineid=line_id).order_by('-openDate')
        context = {'item_list': item_list, 'line_id': line_id}
        return HttpResponseRedirect(reverse('actionitem:detail', args=(line_id,),))

    else:
        form = IssueForm()
    return render(request, 'actionitems/new.html', {'form': form})