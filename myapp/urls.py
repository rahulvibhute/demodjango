from rest_framework.routers import SimpleRouter
from myapp.views import *
router = SimpleRouter()
router.register("Librarian",LibrarianOp)

urlpatterns=router.urls