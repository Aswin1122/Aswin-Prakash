from django.conf.urls.static import static

from todoproject import settings
from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('delete<int:taskid>/',views.delete,name='delete'),
    path('update<int:taskid>/',views.update,name='update'),
    path('cbvhome/',views.Tasklistview.as_view(),name='cbvhome'),
    path('cbvdetail/<int:pk>/',views.Taskdetail.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.Taskupdate.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.Taskdelete.as_view(),name='cbvdelete')
]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
