"""adClick URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
import xadmin
from business import views as business_view
from users import views as users_views
from users.views import LoginView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', xadmin.site.urls),
    url(r'^login/', LoginView.as_view(), name='login'),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^$', users_views.index, name='index'),
    url(r'^createCPM/', business_view.createCPM, name='createCPM'),
    url(r'^CPM/', business_view.CPM),
    url(r'^CPMTask/', business_view.CPMTask, name='CPMTask'),
    url(r'^createCPC/', business_view.createCPC, name='createCPC'),
    url(r'^CPC/', business_view.CPC),
    url(r'^CPCTask/', business_view.CPCTask, name='CPCTask'),
    # url(r'^API/dosql/$', views.dosql, name='ajax_dosql'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
