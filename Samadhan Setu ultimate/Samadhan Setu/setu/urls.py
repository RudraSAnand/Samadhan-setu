from django.urls import path
from . import views

urlpatterns = [
    # Frontend (HTML pages)
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('submit/', views.submit, name='submit'),
    path('track/', views.track, name='track'),
    path('map/', views.map_view, name='map'),
    path('contact/', views.contact, name='contact'),
    path('admin_panel/', views.admin_panel, name='admin_panel'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('faq/', views.faq, name='faq'),
    path("track/", views.track_page, name="track_page"),           # For loading the HTML form
    path("track/status/", views.track_status, name="track_status"),# For AJAX call to fetch status

    # Backend API endpoints (JSON responses)
    path('api/submit-grievance/', views.submit_grievance, name='submit_grievance'),
    path('api/submit-contact/', views.submit_contact, name='submit_contact'),
    path('api/view-grievances/', views.view_grievances, name='view_grievances'),
    path('api/view-contacts/', views.view_contacts, name='view_contacts'),
]
