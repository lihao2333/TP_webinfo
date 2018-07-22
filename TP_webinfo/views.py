from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from navigation.models import Section, Subsection
def index(request):
    sections = Section.objects.all()
    subsections = Subsection.objects.all()
    ctx = {"sections":sections,
            "subsections":subsections}
#    As = [
#            {"name":"a1","id":1,"url":"https://www.baidu.com"},
#            {"name":"a2","id":2,"url":"https://www.baidu.com"},
#            ]
#    Bs = [
#            {"name":"b1","id":1,"url":"https://www.baidu.com"},
#            {"name":"b2","id":2,"url":"https://www.baidu.com"},
#            ]
#    Cs = [
#            {"name":"c1","id":1,"url":"https://www.baidu.com"},
#            {"name":"22","id":2,"url":"https://www.baidu.com"},
#            ]
#    Ds = [
#            {"name":"b1","id":1,"url":"https://www.baidu.com"},
#            {"name":"b2","id":2,"url":"https://www.baidu.com"},
#            ]
#    ctx={"menu":
#            [
#                {"sec":"A",
#                    "subsec":As},
#                {"sec":"B",
#                    "subsec":Bs},
#                {"sec":"C",
#                    "subsec":Cs},
#                {"sec":"D",
#                    "subsec":Ds},
#            ]
#        }
    return render(request,"index.html",ctx)
