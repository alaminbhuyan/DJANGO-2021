# Create our custom filter

from django import template

register = template.Library()


@register.filter(name="remove_special")
def remove_chars(value, args):
    # print("Args: ", args)
    # print("value: ", value)
    for character in args:
        value = value.replace(character, "")
    return value