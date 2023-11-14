from django.urls import path
from .views import TaskList, TaskDetailView, TaskCreateView, TaskDeleteView, TaskUpdateView, TaskImageDeleteView, RegisterView, LoginView, LogoutView
urlpatterns = [
    path('', TaskList.as_view(), name='task_list'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task_details'),
    path('task_form/', TaskCreateView.as_view(), name='task_form'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('task/<int:pk>/update', TaskUpdateView.as_view(), name='task_update'),
    path('task/image/<int:pk>/delete/',
         TaskImageDeleteView.as_view(), name='delete_task_image'),
    path('accounts/register/', RegisterView.as_view(), name='register'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

]
