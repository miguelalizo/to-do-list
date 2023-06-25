from django.urls import path
from .views import UserTaskList, UserTaskDetail, UserTaskCreate, UserTaskUpdate, UserTaskDelete, RegisterPage, task_complete
from django.contrib.auth.views import LogoutView


urlpatterns = [
    # path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('', UserTaskList.as_view(), name='tasks'),
    path('task/<int:pk>', UserTaskDetail.as_view(), name='task'),
    path('task-create/', UserTaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>', UserTaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>', UserTaskDelete.as_view(), name='task-delete'),
    path('task-complete/<int:pk>', task_complete, name='task-complete'),

]