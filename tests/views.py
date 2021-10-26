from django.views.generic import TemplateView
from django.contrib.auth.mixins import PermissionRequiredMixin

from django.http import HttpResponse


class BaseView(PermissionRequiredMixin, TemplateView):
    def get(self, request):
        return HttpResponse("OK")


class HomeView(BaseView):
    permission_required = "tests.view_testauthanonmodel"


class PrivateView(BaseView):
    permission_required = "tests.change_testauthanonmodel"


class SecretView(BaseView):
    permission_required = "tests.delete_testauthanonmodel"
