from django.urls import path


from .views import home, create_letter, tracking_code, tracking_code_entry, view_letter, track_letter_condition, \
    edit_letter, download_pdf

urlpatterns=[
    path('home', home, name='home'),
    path('create_letter/', create_letter, name='create_letter'),
    path('edit/<str:tracking_code>/', edit_letter, name='edit_letter'),
    path('tracking_code/', tracking_code, name='tracking_code'),
    path('tracking_code_entry/', tracking_code_entry, name='tracking_code_entry'),
    path('view_letter/<str:tracking_code>/', view_letter, name='view_letter'),
    path('track_condition/', track_letter_condition, name='track_letter_condition'),
    path('download_pdf/<str:tracking_code>/', download_pdf, name='download_pdf'),


]
