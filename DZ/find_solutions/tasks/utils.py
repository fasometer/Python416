from .models import Task
from django.db.models import Q


def search_task(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    ts = Task.objects.filter(
        Q(title__icontains=search_query) |
        Q(memo__icontains=search_query) |
        Q(lines__line__icontains=search_query)
    )
    return search_query, ts
