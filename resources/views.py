from django.shortcuts import get_object_or_404, render
from .models import ResourceCategory, ResourcePublisher, Resource, Collection


#Request Category Collection Page
def req_category_collections(request, category_id):
    category = get_object_or_404(ResourceCategory, pk=category_id)
    category_collections = Collection.objects.filter(category=category)
    return render(request, 'resources/collections.html', {'category': category, 'collections': category_collections})

def req_category_resources_list(request, category_id):
    all_categories = ResourceCategory.objects.all()
    all_publishers = ResourcePublisher.objects.all()
    category = get_object_or_404(ResourceCategory, pk=category_id)
    category_resources_list = Resource.objects.filter(category=category)
    data = {'all_categories': all_categories, 'all_publishers': all_publishers, 'category': category, 'resources_list': category_resources_list}
    return render(request, 'resources/resources-list.html', data)
