from django import template

register = template.Library()

@register.filter
def subtract(value, arg):
    try:
        # Ensure that both value and arg are numeric (e.g., integers or floats)
        value = int(value)
        arg = int(arg)
        # Perform the subtraction
        result = value - arg
        return result
    except (ValueError, TypeError):
        # Handle exceptions (e.g., if the inputs are not numeric)
        return value  # You can choose to return the original value or handle the error differently
