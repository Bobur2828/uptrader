from django.shortcuts import render
from my_app.templatetags.menu_tags import draw_menu

def index(request):
    menu_name = 'Youtube Видео' #названия
    context = {
        'menu_items': draw_menu(menu_name),
        'active_item': request.path,
    }
    return render(request, 'my_app/index.html', context)
