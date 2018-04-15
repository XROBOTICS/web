from django import forms


class HomeForm(forms.Form):
	post = forms.CharField()
		

	'''def get_post():
		return self.post
		attrs={
		'class': 'form-control',
		'placeholder': 'Write a post...'
		}
	

	class Meta:
		model = Post
		fields = ('post')
'''