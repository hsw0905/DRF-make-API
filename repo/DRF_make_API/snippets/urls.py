from rest_framework.routers import SimpleRouter
from snippets.viewsets import SnippetViewSet

router = SimpleRouter()
router.register(r'snippets', SnippetViewSet, basename='snippets')
urlpatterns = router.urls