from django.urls import path, include
from . import views
app_name='todoapp'
urlpatterns = [


    path('',views.index,name='index'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('chome/',views.TaskListview.as_view(),name='chome'),
    path('cvdetail/<int:pk>/',views.TaskDetailview.as_view(),name='cvdetail'),
    path('cupdate/<int:pk>/',views.TaskUpdateView.as_view(),name='cupdate'),
    path('cdelete/<int:pk>/',views.TaskDeleteView.as_view(),name='cdelete')
]
