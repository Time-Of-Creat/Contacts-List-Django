from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from .models import Contact


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')


def home(request):
    context = {
        'total_contacts': Contact.objects.count() if hasattr(Contact, 'objects') else 0,
        'recent_contacts': Contact.objects.filter(
            # Фильтр по дате добавления, если есть поле created_at
        ).count() if hasattr(Contact, 'objects') else 0,
    }
    return render(request, 'contacts/home.html', context)