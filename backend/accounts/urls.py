from django.urls import path, include
from .views import TwitterLogin,GoogleLogin,UserRedirectView


urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('registration/', include('dj_rest_auth.registration.urls')),
    path('twitter/', TwitterLogin.as_view(), name='twitter_login'),
    path('google/', GoogleLogin.as_view(), name='google_login'),
    path("~redirect/", view=UserRedirectView.as_view(), name="redirect")
    
]