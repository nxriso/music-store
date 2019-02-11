from django import template

register = template.Library()


@register.inclusion_tag('home/tags/home_slide.html')
def render_slide(slide):
    return {
        'slide': slide,
    }
