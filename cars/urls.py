from django.contrib import admin
from django.http import HttpRequest, HttpResponse
from django.urls import path
from app.views import show_cars, delete_car, add_car


def show_index(request: HttpRequest) -> HttpResponse:
    return HttpResponse(
        """
        <HTML>
        <body>
            <h1>Hello, this is index!</h1>
            <p><a href="/cats">Cats</a></p>
            <p><a href="/cars">Cars</a></p>
            <p><a href="//tengrinews.kz">Tengrinews</a></p>
        </body>
        </HTML>
        """
    )


def show_cats(request: HttpRequest) -> HttpResponse:
    return HttpResponse("""
    <HTML>
        <body>
            <h1>Hello, cats!</h1>
            <p>This is the home page for cats.</p>
        </body>
    </HTML>
    """)


urlpatterns = [
    path('', show_index),
    path('cats', show_cats),
    path('cars', show_cars),
    path('cars/<int:id_>/delete', delete_car),
    path('cars/add', add_car),
    path('admin/', admin.site.urls),
]
