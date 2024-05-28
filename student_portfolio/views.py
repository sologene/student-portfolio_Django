from django.views.generic import ListView
from .models import Apps
from django.shortcuts import render


class Main_View(ListView):
    model = Apps
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['app_list'] = Apps.objects.all()  # Assuming YourModel is the model you are querying
        return context


def about(request):
    return render(request,"about.html")
