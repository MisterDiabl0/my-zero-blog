# <<<<<<< HEAD
from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

# # print
# =======
# from django import forms
#
# from .models import Post
#
# class PostForm(forms.ModelForm):
#
#     class Meta:
#         model = Post
#         fields = ('title', 'text',)
#
# # print
# >>>>>>> e21252fb01dc74cf003eb0e2e9b22aab8a2dcd45
