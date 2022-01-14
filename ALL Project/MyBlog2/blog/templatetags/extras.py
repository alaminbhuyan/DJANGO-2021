# Create a Custom filter tag

from django import template

register = template.Library()

@register.filter(name='get_val')
# Parameters: dic = replyDict, key = comment.sno
def get_val(dic, key):
    return dic.get(key)