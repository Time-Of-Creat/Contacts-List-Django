from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Contact
from .forms import ContactForm


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')


def home(request):
    context = {
        'total_contacts': Contact.objects.count() if hasattr(Contact, 'objects') else 0,
        'recent_contacts': Contact.objects.filter(
        ).count() if hasattr(Contact, 'objects') else 0,
    }
    return render(request, 'contacts/home.html', context)


@login_required
def contact_list(request):
    contacts = Contact.objects.filter(user=request.user).order_by('-creation_date')
    return render(request, 'contacts/contact_list.html', {'contacts': contacts})


@login_required
def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            messages.success(request, f'Контакт "{contact}" успешно создан!')
            return redirect('contact_list')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
    else:
        form = ContactForm()
    
    return render(request, 'contacts/contact_form.html', {
        'form': form,
        'title': 'Создание контакта',
        'button_text': 'Создать контакт',
        'action': 'create'
    })