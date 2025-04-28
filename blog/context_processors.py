from .models import Category

def categories_context(request):
    categories = Category.objects.all()
    active_category = request.GET.get('category', '')
    return {
        'categories': categories,
        'active_category': active_category,
    }