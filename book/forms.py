from django import forms
from .models import Book
#DataFlair
class BookCreate(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class DateRangeForm(forms.Form):
	start_date = forms.DateField(widget=forms.TextInput(attrs=
		{
			'class':'datepicker'
		}))
	end_date = forms.DateField(widget=forms.TextInput(attrs=
		{
			'class':'datepicker'
		}))