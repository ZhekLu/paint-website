from django.urls import path

from paintsite.views import index, other_page, PSLoginView, profile, PSLogoutView, ChangeUserInfoView, \
    PSPasswordChangeView, RegisterUserView, RegisterDoneView, user_activate

app_name = 'paintsite'

urlpatterns = [
    path('accounts/logout/', PSLogoutView.as_view(), name='logout'),
    path('accounts/password/change', PSPasswordChangeView.as_view(), name='password_change'),
    path('accounts/profile/change', ChangeUserInfoView.as_view(), name='profile_change'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/register/activate/<str:sign>/', user_activate, name='register_activate'),
    path('accounts/register/done/', RegisterDoneView.as_view(), name='register_done'),
    path('accounts/register/', RegisterUserView.as_view(), name='register'),
    path('accounts/login/', PSLoginView.as_view(), name='login'),
    path('<str:page>/', other_page, name='other'),
    path('', index, name='index'),
]
