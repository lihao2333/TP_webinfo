from django.contrib import admin
from navigation.models import Section,Subsection,Block
class SecAdmin(admin.ModelAdmin):
        list_display = ('name',)
class SubsecAdmin(admin.ModelAdmin):
        list_display = ('name','section', 'url')
class BlockAdmin(admin.ModelAdmin):
        list_display = ('image','title','content')
admin.site.register(Section,SecAdmin)
admin.site.register(Subsection,SubsecAdmin)
admin.site.register(Block,BlockAdmin)
