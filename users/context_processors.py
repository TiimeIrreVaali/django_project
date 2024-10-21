from core.views import menu


def get_core_context(request):
    return {'mainmenu': menu}