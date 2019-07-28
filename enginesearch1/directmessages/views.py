from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Message
from django.contrib import messages
#from cart.forms import CartAddProductForm
#from django.db.models import Q
from django.contrib.auth.models import User
#from .config import pagination
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpRequest, HttpResponseRedirect
from django.db.models import Count
from .forms import *
from directmessages.apps import Inbox

app_name = 'directmessages'

@login_required(login_url="/account/login")
def Send_message(request):
    messages1 = Message.objects.filter(recipient=request.user).order_by("-sent_at")
    if request.method == 'POST':
        form = Messageform(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.sender = request.user
            instance.save()
            messages.success(request, 'Message succesfully sent')
            return HttpResponseRedirect('message')

        else:
            messages.error(request, 'Invalid entry. Please check the fields')

    else:
        form = Messageform()

    return render(request, 'directmessage/message.html', {'form_message': form,'messages':messages1})


# @login_required(login_url="/account/login")
# def message(request):
#     messages = Message.objects.filter(recipient=request.user)
#     context = {
#         'messages':messages,
#     }
#     return render(request, 'directmessage/message.html', context)






