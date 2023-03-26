import django.forms

import core.forms
import rating.models


class RatingForm(django.forms.ModelForm, core.forms.BootstrapFormMixin):
    class Meta:
        model = rating.models.Rating

        fields = (rating.models.Rating.rating.field.name,)

        labels = {
            rating.models.Rating.rating.field.name: (
                rating.models.Rating.rating.field.verbose_name.capitalize()
            ),
        }

        widgets = {
            rating.models.Rating.rating.field.name: django.forms.Select(
                attrs={
                    'class': 'form-select mb-4',
                },
            )
        }
