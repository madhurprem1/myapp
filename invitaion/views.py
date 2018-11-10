from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages


class IndexView(TemplateView):
    # queryset = CommandExecution.objects.all()
    template_name = "index.html"
    print("HHII")

class ContactView(TemplateView):
    # queryset = CommandExecution.objects.all()
    template_name = "contact.html"
    