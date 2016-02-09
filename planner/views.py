from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template.context import RequestContext

from django.contrib.auth.models import User
from .models import Task
import unicodedata
import json


def viewHome(request):
    context = RequestContext(request)
    context.update({ 'msg_body' : "Task Planner", })

    if request.method == "POST":
        taskname = request.POST.get('taskname', None)
        taskstatus = request.POST.get('taskstatus', None)
        taskcost = request.POST.get('taskcost', None)
        editmode = request.POST.get('editmode', False)

        if taskcost and taskname and taskstatus:
            try:
                if editmode:
                    ntask = Task.objects.filter(id=editmode).update(name=taskname, status=taskstatus, cost=taskcost)
                else:
                    ntask = Task(name=taskname, status=taskstatus, cost=taskcost)

                ntask.save()
            except:
                context.update({ 'messages' : ['Task details save failed'], })

    ptasks = Task.objects.all()
    context.update({ 'ptasks' : ptasks, })

    return render_to_response("home.html", context_instance=context)

def viewEdit(request):
    context = RequestContext(request)
    context.update({'msg_body' : "Edit Task"})

    ptasks = Task.objects.all()
    context.update({ 'ptasks' : ptasks, })

    return render_to_response("home.html", context_instance=context)