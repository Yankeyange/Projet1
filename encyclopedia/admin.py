from django.contrib import admin
from encyclopedia.models import Topic

class TopicAdmin(admin.ModelAdmin):
  list_display = ("name","first_name","description")

admin.site.register(Topic, TopicAdmin)
