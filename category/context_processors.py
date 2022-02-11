#takes req as an argument and returns dictionary as a context
#tell settings we are using this


from .models import Category

def menu_links(request):
    links = Category.objects.all()

    return dict(links=links)