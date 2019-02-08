from django import template

register = template.Library()


@register.inclusion_tag('famous_clients/tags/famous_clients_slideshow.html')
def render_client_slideshow(clients):
    return {
        'clients': clients,
    }
