from django import template


register = template.Library()


def get_element(value, count):
    return value[count]


register.filter('get_element', get_element)
