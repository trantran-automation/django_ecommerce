from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('signup/', views.register, name='signup'),
    # path('signin/', views.sign_in, name='signin'),
    path('login/', LoginView.as_view(template_name='registration/signin.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='store'), name='logout'),
]