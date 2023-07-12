
from django.contrib import admin
from .models import PROFILE, PUBLICATION, COMMENTS, TAGS

admin.site.register(PROFILE)
admin.site.register(PUBLICATION)
admin.site.register(COMMENTS)
admin.site.register(TAGS)
