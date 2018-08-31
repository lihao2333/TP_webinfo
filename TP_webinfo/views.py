from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from navigation.models import Section, Subsection,Block,Main
def index(request):
    sections = Section.objects.all()
    subsections = Subsection.objects.all()
    blocks = Block.objects.all()
    main = Main.objects.all()[0]
    ctx = {"sections":sections,
            "subsections":subsections,
            "blocks":blocks,
            "main":main
            }
#    As = [
#            {"name":"a1","id":1,"url":"https://www.baidu.com"},
#            {"name":"a2","id":2,"url":"https://www.baidu.com"},
#            ]
#    Bs = [
#            {"name":"b1","id":1,"url":"https://www.baidu.com"}, #            {"name":"b2","id":2,"url":"https://www.baidu.com"},
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
def content(request,subsection_id):
    cur_subsection = Subsection.objects.filter(id=subsection_id)[0]
    cur_section = Section.objects.filter(id=cur_subsection.section.id)[0]
    cur_content = cur_subsection.content.replace('\r\n','\\n')
    sections = Section.objects.all()
    subsections = Subsection.objects.all()
    main = Main.objects.all()[0]
    ctx = {"cur_section":cur_section,
            "cur_subsection":cur_subsection,
            "cur_content":cur_content,
            "sections":sections,
            "subsections":subsections,
            "main":main
            }
    return render(request,"content.html",ctx)
#    return HttpResponse("%d"%content_id)

