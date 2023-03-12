from django.conf import settings
from django.core.mail import send_mail
import django.shortcuts

import feedback.forms


def feedback_form(request):
    template = 'feedback/feedback.html'
    form = feedback.forms.FeedbackForm(request.POST or None)

    if form.is_valid():
        text = form.cleaned_data.get('text')
        email = form.cleaned_data.get('email')
        send_mail(
            'Subject',
            text,
            settings.EMAIL,
            [email],
            fail_silently=False,
        )
        return django.shortcuts.redirect('feedback:success')
    context = {
        'forms': form,
    }
    return django.shortcuts.render(request, template, context)


def success(request):
    template = 'feedback/success.html'
    return django.shortcuts.render(request, template)
