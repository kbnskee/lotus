from django import template

register = template.Library()


@register.filter
def kdr_split_first(value):
    return value.split(" ",1)[0]