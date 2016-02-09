from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template.context import RequestContext

from django.contrib.auth.models import User
from .models import Task
import unicodedata
import json


def home(request):
    context = RequestContext(request)
    context.update({ 'msg_body' : "Task Planner", })

    ptasks = Task.objects.all()
    context.update({ 'ptasks' : ptasks, })

    return render_to_response("home.html", context_instance=context)