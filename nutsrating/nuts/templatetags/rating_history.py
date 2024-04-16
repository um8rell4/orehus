from nuts.models import OrehusChange, CustomUser
from django import template

register = template.Library()


@register.simple_tag()
def rating_logs():
    return OrehusChange.objects.all()


@register.filter
def subtract(value, arg):
    return value - arg
