import re
from django import template

register = template.Library()
STRING_THAT_NEVER_OCCURS = '#f4x@SgXXmS'

def search(value, search):
    return re.sub(search, STRING_THAT_NEVER_OCCURS, value)

def replace(value, replace):
    return re.sub(STRING_THAT_NEVER_OCCURS, replace, value)

register.filter(search)
register.filter(replace)