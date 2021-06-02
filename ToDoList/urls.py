from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name="home"),
    path('register/', views.UserRegisterView.as_view(), name="register"),
    path('edit_user/', views.UserEditView.as_view(),  name="edit_user"),
    path('password/', views.PasswordsChangeView.as_view(), name="password_change"),
    path('tasks/', views.TaskView.as_view(), name="task_view"),
    path('create_task/', views.CreateTaskView.as_view(), name="create_task"),
    path('edit_task/<int:pk>', views.EditTaskView.as_view(), name="edit_task"),
    path('delete_task/<int:pk>', views.DeteletaskView.as_view(), name="delete_task"),

]
