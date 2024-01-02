from django import template

register = template.Library()

@register.filter(name='get_section_by_level')
def get_section_by_level(list, value):
    
    return '#row' + str(value)