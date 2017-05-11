from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value, arg):
    """
Ta funkcja wycina z wartosci argument
    """

    return value.replace(arg,'')

# register.filter('cut',cut)
