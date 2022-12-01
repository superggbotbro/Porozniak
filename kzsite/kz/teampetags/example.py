from django import template
from kz.models import *

register = template.Library()


@register.simple_tag()
def get_catigories():
    return Category.objects.all()