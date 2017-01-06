from django import template
register = template.Library()

#Create your filter functions
#Doc: https://docs.djangoproject.com/en/dev/howto/custom-template-tags/#writing-custom-template-filters
#Help: http://stackoverflow.com/questions/8000022/django-template-how-to-look-up-a-dictionary-value-with-a-variable
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
