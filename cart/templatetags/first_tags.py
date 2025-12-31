from django import template
from django.template.loader import get_template

register = template.Library()

def my_template(value, arg):
    
        return value*arg



register.filter('multiply', my_template)
