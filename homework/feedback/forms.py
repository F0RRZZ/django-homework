import django.forms

import feedback.models


class FeedbackForm(django.forms.ModelForm):
    email = django.forms.EmailField(
        widget=django.forms.EmailInput(
            attrs={'placeholder': 'example@example.com'},
        ),
        label='Ваша почта',
        error_messages={'reqired': ''},
        help_text='введите почту, на которую будет отправлен ответ'
    )
    files = django.forms.FileField(
        widget=django.forms.ClearableFileInput(
            attrs={'multiple': True}
        ),
        required=False,
        label='Файлы',
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = feedback.models.Feedback
        fields = (
            feedback.models.Feedback.text.field.name,
        )
        labels = {
            feedback.models.Feedback.text.field.name: 'Текст',
        }
        widgets = {
            feedback.models.Feedback.text.field.name: django.forms.Textarea(
                attrs={'rows': 5},
            ),
        }

    def clean_text(self):
        text = self.cleaned_data['text']
        return text.strip()
