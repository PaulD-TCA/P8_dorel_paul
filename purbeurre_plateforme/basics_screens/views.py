from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# Create your views here.
def legal_notice(request):

    template = loader.get_template('basics_screens/legal_notice_page.html')
    context = {}
    # return HttpResponse("Hello, search.")
    return HttpResponse(template.render(context, request))
