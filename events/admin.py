from django.contrib import admin

from .models import Topic, Event, City, EventTopic, UserSearchHistory

admin.site.register(Topic)
admin.site.register(Event)
admin.site.register(City)
admin.site.register(EventTopic)
admin.site.register(UserSearchHistory)
