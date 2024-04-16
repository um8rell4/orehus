from nuts.models import CustomUser
from django import template

register = template.Library()


@register.inclusion_tag('templatetags/_leaderboard.html')
def show_leaderboard():
    users = CustomUser.objects.all()
    return {'users': users}
