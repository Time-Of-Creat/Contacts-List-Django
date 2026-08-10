from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

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


@login_required
def contact_list(request):
    contacts = Contact.objects.filter(user=request.user).order_by('-creation_date')
    return render(request, 'contacts/contact_list.html', {'contacts': contacts})
