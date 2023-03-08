from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from . import *
from . models import Task
from . forms import todoform
from django . views.generic import ListView
from django . views.generic.detail import DetailView
from django . views.generic.edit import UpdateView,DeleteView
# Create your views here.

class Tasklistview(ListView):
    model=Task
    template_name = 'index.html'
    context_object_name = 'task1'

class Taskdetail(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task'

class Taskupdate(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})

class Taskdelete(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')




def index(request):
    task1 = Task.objects.all()
    if request.method=='POST':
        na=request.POST.get('name','')
        pri=request.POST.get('priority','')
        da=request.POST.get('date','')
        task=Task(name=na,priority=pri,date=da)
        task.save()
    return render(request,'index.html',{'task1':task1})

def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method=="POST":
        task.delete()
        return redirect('/')


    return render(request,'delete.html')

def update(request,taskid):
    task=Task.objects.get(id=taskid)
    fo=todoform(request.POST or None, instance=task)
    if fo.is_valid():
        fo.save()
        return redirect('/')
    return render(request,'edit.html',{'fo':fo,'task':task})