from .models import Task
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


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


def paginate_projects(request, ts, results):
    page = request.GET.get('page')
    # results = 3
    paginator = Paginator(ts, results)

    try:
        ts = paginator.page(page)
    except PageNotAnInteger:  # http://127.0.0.1:8000/projects/?page=assa
        page = 1
        ts = paginator.page(page)
    except EmptyPage:  # http://127.0.0.1:8000/projects/?page=100000
        page = paginator.num_pages  # последняя страница
        ts = paginator.page(page)

    left_index = int(page) - 4
    if left_index < 1:
        left_index = 1
    right_index = int(page) + 5
    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1

    custom_range = range(left_index, right_index)
    return custom_range, ts
