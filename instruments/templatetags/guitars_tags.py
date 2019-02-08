from django import template

register = template.Library()


@register.inclusion_tag('instruments/tags/guitars.html')
def render_guitars(guitars):
    return{
        'guitars': guitars,
    }
