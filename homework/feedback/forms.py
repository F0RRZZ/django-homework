import django.forms

import feedback.models


class FeedbackForm(django.forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = feedback.models.Feedback
        fields = (
            feedback.models.Feedback.text.field.name,
            feedback.models.Feedback.email.field.name,
        )
        labels = {
            feedback.models.Feedback.text.field.name: 'Текст',
            feedback.models.Feedback.email.field.name: 'Ваша почта',
        }
        widgets = {
            feedback.models.Feedback.text.field.name: django.forms.Textarea(
                attrs={'rows': 5}
            ),
            feedback.models.Feedback.email.field.name: django.forms.EmailInput(
                attrs={'placeholder': 'example@example.com'}
            ),
        }
