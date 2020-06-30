from allauth.account.views  import SignupView
from .forms import MySignupForm
from django import forms

class ProfileSignupView(SignupView):
    template_name="account/signup.html"
    success_url=''
    form_class=None
    profile_class=None
    
    def form_valid(self,form):
        response=super(ProfileSignupView,self).form_valid(form)
       
        return response

     


