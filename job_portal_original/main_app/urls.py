from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('post_login/', views.post_login, name="post_login"),
    path('register/', views.register, name="register"),
    path('post_register/', views.post_register, name="post_register"),
    path('mainpage/', views.main_page, name="mainpage"),
    path('resume/', views.resume, name="resume"),
    path('alerts/', views.alerts, name="alerts"),
    path('job_list/', views.job_list, name="job_list"),
    path('logout/', views.logout, name="logout"),

    path('job_seeker/', views.job_seeker, name="job_seeker"),
    path('jobs/', views.jobs, name="jobs"),
    path('activity_logs/', views.activity_logs, name="activity_logs"),
    path('company/', views.company, name="company"),

    path('company_register/', views.company_register, name="company_register"),
    path('post_company_register/', views.post_company_register, name="post_company_register"),
    path('company_mainpage/', views.company_mainpage, name="company_mainpage"),

    #crud
    path('edit_resue/', views.edit_resume, name="edit_resume"),
    path('apply_job/', views.apply_job, name="apply_job"),
    path('delete_user/', views.delete_user, name="delete_user"),
    path('delete_job/', views.delete_job, name="delete_job"),
    path('edit_job/', views.edit_job, name="edit_job"),
    path('edit_company/', views.edit_company, name="edit_company"),
    path('delete_company/', views.delete_company, name="delete_company"),
    path('add_job/', views.add_job, name="add_job"),
    path('search_job/', views.search_job, name="search_job"),
    path('filter_job/', views.filter_job, name="filter_job"),
]
