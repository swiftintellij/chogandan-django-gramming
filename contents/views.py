from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from contents.models import Gram, Image
from users.views import ApiView


class HomeView(LoginRequiredMixin, TemplateView):
    # @method_decorator(login_required)
    # def dispatch(self, request, *args, **kwargs):
    #     return super(HomeView, self).dispatch(request, args, kwargs)
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        user = self.request.user
        context['contents'] = Gram.objects.select_related("user").prefetch_related("image_set").filter(
            user__id=user.id
        )
        return context


@method_decorator(login_required, name="dispatch")
class GramAddView(ApiView):
    def post(self, request):
        content = request.POST.get("content", "").strip()
        gram = Gram.objects.create(user=request.user, content=content)
        for index, file in enumerate(request.FILES.values()):
            Image.objects.create(content=gram, resource=file, order=(1 + index))
        return self.response()
