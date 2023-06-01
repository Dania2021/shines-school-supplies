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

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'placeholder': 'Title'})
        self.fields['content'].widget.attrs.update(
            {'placeholder': 'Content'})

        self.fields['title'].widget.attrs['autofocus'] = True
        self.fields['title'].widget.attrs['class'] = 'border-black'
        self.fields['content'].widget.attrs['class'] = 'border-black'
        self.fields['title'].label = False
        self.fields['content'].label = False

    rating = forms.ChoiceField(label='How will you rate this product?',
                               choices=RATINGS,
                               widget=forms.RadioSelect)
