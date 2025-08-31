"""
URL configuration for find_solutions project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tasks import views
from django.conf.urls.static import static  # подключение изо
from django.conf import settings   # подключение изо

urlpatterns = [
    path('admin/', admin.site.urls),
    # Auth
    path('signup/', views.signup_user, name='signupuser'),
    path('logout/', views.logout_user, name='logoutuser'),
    path('login/', views.login_user, name='loginuser'),

    # Tasks
    path('current/', views.current_tasks, name='currenttasks'),
    path('', views.home, name='home'),
    path('create/', views.create_task, name='createtask'),
    path('tasks/<int:tasks_pk>/', views.view_task, name='viewtask'),
    path('tasks/<int:tasks_pk>/complete', views.complete_task, name='completetask'),
    path('completed/', views.completed_tasks, name='completedtasks'),
    path('tasks/<int:tasks_pk>/delete', views.delete_task, name='deletetask'),
    path('tasks/inbox.html', views.inbox, name='inbox'),
]

# подключение изо
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)