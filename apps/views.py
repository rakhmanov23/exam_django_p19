from django.shortcuts import render

from apps.models import Contact


# Create your views here.


def index_view(request):
    context = {
        'contacts': Contact.objects.all()
    }
    return render(request, 'apps/index.html', context)
