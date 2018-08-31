from django.contrib import admin
from navigation.models import Section,Subsection,Block,Main,Images
class SecAdmin(admin.ModelAdmin):
        list_display = ('name',)
class SubsecAdmin(admin.ModelAdmin):
        list_display = ('name','section')
class BlockAdmin(admin.ModelAdmin):
        list_display = ('image','title','content')
class ImagesAdmin(admin.ModelAdmin):
        list_display = ('id','image')
class MainAdmin(admin.ModelAdmin):
        list_display = ('title','welcome','welcome_sub','wallpaper','logo','tele','weibo','email','address')
admin.site.register(Section,SecAdmin)
admin.site.register(Subsection,SubsecAdmin)
admin.site.register(Block,BlockAdmin)
admin.site.register(Images,ImagesAdmin)
admin.site.register(Main,MainAdmin)
