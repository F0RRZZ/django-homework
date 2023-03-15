import os

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
import django.shortcuts

import feedback.forms
import feedback.models


def feedback_form(request):
    template = 'feedback/feedback.html'
    form = feedback.forms.FeedbackForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            text = form.cleaned_data.get('text')
            email = form.cleaned_data.get('email')
            personal_data = feedback.models.PersonalData(email=email)
            personal_data.save()
            new_feedback = feedback.models.Feedback(
                text=text,
                personal_data=personal_data,
            )
            new_feedback.save()
            if request.FILES.getlist('files'):
                feedback_dir = os.path.join('uploads', str(new_feedback.id))
                os.makedirs(feedback_dir)
                for file in request.FILES.getlist('files'):
                    file_system = FileSystemStorage(location=feedback_dir)
                    filename = file_system.save(file.name, file)
                    feedback_file = feedback.models.FeedbackFile(
                        feedback=new_feedback,
                        file=filename,
                    )
                    feedback_file.save()
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
