from django.urls import path
from .views import( workout_session_list, workout_session_detail,
                   client_list, client_detail, 
                   trainer_list, trainer_detail,
                   gym_list, gym_detail)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # JWT Tokens
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Gym
    path('gyms/', gym_list, name='gym-list'),
    path('gyms/<int:pk>/', gym_detail, name='gym-detail'),
    
    # Trainers
    path('trainers/', trainer_list, name='trainer-list'),
    path('trainers/<int:pk>/', trainer_detail, name='trainer-detail'),
    
    # Clients
    path('clients/', client_list, name='client-list'),
    path('clients/<int:pk>/', client_detail, name='client-detail'),    
    
    # workout-sessions
    path('workouts/', workout_session_list, name='workout-session-list'),
    path('workouts/<int:pk>/', workout_session_detail, name='workout-session-detail'),
]
