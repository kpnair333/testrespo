from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from . models import Task
from . forms import Todoform
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView,DeleteView

class Tasklistview(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task1'

class TaskDetailview(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'task'

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','age')

    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})
class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')











def add(request):
    task1 = Task.objects.all()
    if(request.method=="POST"):
        name=request.POST['task']
        priority=request.POST['priority']
        date=request.POST.get('date')
        task=Task(name=name,priority=priority,date=date)
        task.save()
    return render(request,'home.html',{'task1':task1})
# def details(request):
#
#     return render(request,'details.html')
def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def cancel(request):
    if request.method=='POST':
        return redirect('/')


def update(request,id):
    task = Task.objects.get(id=id)
    f = Todoform(request.POST or None,instance = task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'f':f,'task':task})