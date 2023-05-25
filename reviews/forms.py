from django import forms
from .models import Review

RATINGS = [(1, 'Worst'),
           (2, 'Bad'),
           (3, 'Ok'),
           (4, 'Good'),
           (5, 'Awesome!')]


class ReviewForm(forms.ModelForm):
    """ Form for leaving rating and review """

    class Meta:
        model = Review
        fields = ('title', 'content', 'rating')

    rating = forms.ChoiceField(label='How will you rate this product?',
                               choices=RATINGS,
                               widget=forms.RadioSelect)
