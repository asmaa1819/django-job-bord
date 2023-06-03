
from django.urls import path , include
from . import views
from . import api 
app_name='job'
urlpatterns = [
    path('',views.job_list ,name='job_list' ),
    path('add', views.add_job, name='add_job'), 
    path('<str:slug>', views.job_detail, name='job_detail'),
    
    path('api/list', api.job_list_api, name='job_list_api'), #API URL
    path('api/list/<int:id>', api.job_detail_api, name='job_detail_api'), #API 
    
    #class based views in API
    path('api/v2/list', api.JobListApi.as_view(), name='Job_List_Api'),
     path('api/v2/list/<int:id>', api.JobDetailApi.as_view(), name='Job_detail_Api'),
    
    
]