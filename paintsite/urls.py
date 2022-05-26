from django.urls import path

from paintsite.views import index, other_page, PSLoginView, profile, PSLogoutView, ChangeUserInfoView

app_name = 'paintsite'

urlpatterns = [
    path('accounts/logout/', PSLogoutView.as_view(), name='logout'),
    path('accounts/profile/change', ChangeUserInfoView.as_view(), name='profile_change'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/login/', PSLoginView.as_view(), name='login'),
    path('<str:page>/', other_page, name='other'),
    path('', index, name='index'),
]
