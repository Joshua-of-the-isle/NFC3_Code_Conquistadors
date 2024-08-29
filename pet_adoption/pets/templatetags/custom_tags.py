# myapp/templatetags/custom_tags.py

from django import template

register = template.Library()

@register.filter
def is_in_group(user, group_name):
    if user.is_authenticated:
        return user.groups.filter(name=group_name).exists()
    return False

