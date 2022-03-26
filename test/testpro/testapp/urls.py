from django.urls import path

from testapp import views
app_name='testapp'
urlpatterns = [
    path('',views.home,name='home'),
    path('test/<int:mobile_id>/',views.detail,name='detail'),
    path('add/',views.add,name='add'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')
]