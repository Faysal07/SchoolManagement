"""
URL configuration for SchoolManagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# Statis Image  Link up
from django.conf.urls.static import static
# Media Image Link up
from django.conf import settings


# Link the File Form Views
from notice.views import noticeLists
from schoolmember.views import MemberListsView, MemberDetailView, MemberCreateView, MemberUpdateView, MemberDeleteView

from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Create my URLS Link Here
    path('notices/', noticeLists, name="noticeLists"),
    
    # Member Urls
    path('members/', MemberListsView.as_view(), name='members'),
    path('members/<int:pk>/', MemberDetailView.as_view(), name='memberdetails'),
    path('members/create/', MemberCreateView.as_view(), name='memberinput'),
    path('members/<int:pk>/update/', MemberUpdateView.as_view(), name="memberedit"),
    path('members/<int:pk>/delete/', MemberDeleteView.as_view(), name="memberdelete")
 
]


# Image debug Code
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
