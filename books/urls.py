from rest_framework.routers import DefaultRouter
from .views import BookSetView, ExchangeSetView, CitySetView, GenreSetView
router = DefaultRouter()

router.register('book',BookSetView, basename='book')
router.register('exchange',ExchangeSetView, basename='exchange')
router.register('city',CitySetView, basename='city')
router.register('genre',GenreSetView, basename='genre')

urlpatterns = router.urls
