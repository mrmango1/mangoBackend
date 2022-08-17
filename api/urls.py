from django.urls import path
from api.views import MangaView

urlpatterns = [
    path('manga/', MangaView.as_view(), name='manga_list'),
    path('manga/<int:num>',
         MangaView.as_view(), name='manga_num'),
]
