from django import template

register = template.Library()

@register.filter(name='first_three_chars')
def first_three_chars(value):
    return value[:3]