from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template.context import RequestContext

from django.contrib.auth.models import User
from .models import Task
import sys
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
                if editmode and editmode != "False":
                    ntask = Task.objects.filter(id=editmode).update(name=taskname, status=taskstatus, cost=taskcost)
                    if ntask:
                        context.update({ 'messages' : ['Task details saved successfully.'], })
                    else:
                        context.update({ 'messages' : ['Task details saved failed.'], })
                else:
                    ntask = Task(name=taskname, status=taskstatus, cost=taskcost)
                    ntask.save()
                    context.update({ 'messages' : ['Task details saved successfully.'], })
            except:
                context.update({ 'messages' : ['Task details save failed'], })

    ptasks = Task.objects.all()
    context.update({ 'ptasks' : ptasks, 'taskid' : False })

    return render_to_response("home.html", context_instance=context)

def viewEdit(request, **Args):
    context = RequestContext(request)
    context.update({'msg_body' : "Edit Task"})

    taskid = int(str(Args.get('taskid')).strip('/'))

    etask = Task.objects.get(pk=taskid)

    ptasks = Task.objects.all()
    context.update({ 'ptasks' : ptasks, 'taskid' : taskid, 'etask' : etask })

    return render_to_response("home.html", context_instance=context)