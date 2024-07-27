from django import template
from my_app.models import Menu, MenuItem

register = template.Library()

@register.simple_tag
def draw_menu(menu_name):
    try:
        menu = Menu.objects.get(name=menu_name)
    except Menu.DoesNotExist:
        return []

    items = MenuItem.objects.filter(menu=menu).select_related('parent')
    menu_dict = {}
    for item in items:
        if item.parent:
            if item.parent.id not in menu_dict:
                menu_dict[item.parent.id] = {'parent': item.parent, 'children': []}
            menu_dict[item.parent.id]['children'].append(item)
        else:
            menu_dict[item.id] = {'parent': item, 'children': []}

    root_items = [item for item in menu_dict.values() if not item['parent'].parent]
    return root_items
