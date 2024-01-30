from django import forms

from catalog.models import Product, Version


class StyleFormMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        # fields = '__all__'
        fields = ('name', 'category', 'description', 'img', 'cost',)

    censored = ['казино',
                'криптовалюта',
                'крипта',
                'биржа',
                'дешево',
                'бесплатно',
                'обман',
                'полиция',
                'радар'
                ]



    def clean_name(self):
        cleaned_data = self.cleaned_data['name']


        for word in self.censored:
            if word in cleaned_data:
                raise forms.ValidationError('Не существет техники с таким названием')

            return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')
        for word in self.censored:
            if word in cleaned_data:
                raise forms.ValidationError(f'Недопустимое слово - {word}!')

        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'
