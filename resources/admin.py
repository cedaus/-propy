from django.contrib import admin
from .models import ResourceCategory, ResourceTag, ResourcePublisher, Resource, Collection, ResourceCollectionAssociation

# Register your models here.
admin.site.register(ResourceCategory)
admin.site.register(ResourceTag)
admin.site.register(ResourcePublisher)
admin.site.register(Resource)
admin.site.register(Collection)
admin.site.register(ResourceCollectionAssociation)
