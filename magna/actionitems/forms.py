from django import forms

from .models import Issue

class IssueForm(forms.ModelForm):

		class Meta:
				model = Issue
				fields = ('lineid','item', 'scrap', 'status','openDate', 'rootCause','team','targetDate' ,'closeDate', 'problem')

class SearchForm(forms.ModelForm):

		class Meta:
				model = Issue
				fields = ('team',)
