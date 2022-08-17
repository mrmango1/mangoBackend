from typing import Any
from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponseBase
from django.views import View
from api.models import Manga
from django.http import HttpRequest
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .scrape.getMangas import getMangas

# Create your views here.


class MangaView(View):
    @method_decorator(csrf_exempt)
    def dispatch(
        self, request: HttpRequest, *args: Any, **kwargs: Any
    ) -> HttpResponseBase:
        return super().dispatch(request, *args, **kwargs)

    # def get(self, request: HttpRequest) -> JsonResponse:
    #     mangas = list(Manga.objects.values())
    #     if len(mangas)>0:
    #         datos = {'message': 'Success', 'manga' : mangas}
    #     else:
    #         datos = {'message': 'Mangas not found'}
    #     return JsonResponse(datos)

    def get(self, request: HttpRequest, num: int = 20,  webPage: str = "mangacrab.com") -> JsonResponse:
        mangas = getMangas(num, webPage)
        if len(mangas) > 0:
            datos = {"message": "Success", "manga": mangas}
        else:
            datos = {"message": "Mangas not found"}
        return JsonResponse(datos)

    def post(self, request: HttpRequest):
        pass

    def put(self, request: HttpRequest):
        pass

    def delete(self, request: HttpRequest):
        pass
