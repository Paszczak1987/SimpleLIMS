from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from building_site.models import BuildingSite


# Create your views here.

class BuildingSiteView(LoginRequiredMixin, DetailView):
    model = BuildingSite
    template_name = 'building_site/building_site.html'
    context_object_name = 'building_site'
