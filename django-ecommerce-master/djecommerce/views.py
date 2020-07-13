from core.models import UserProfile
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from allauth.account.decorators import verified_email_required
from django.shortcuts import render

@verified_email_required
@login_required
def login_success(request):
    """
    Redirects user to various pages depending on whether they
    are customers or retailers
    """
    try:
        user=UserProfile.objects.get(
                user=request.user)
        
        if user.is_retailer:
            return redirect('seller:admin_view')
        else:
            return redirect('core:home')
    except:
        return render(request,"404.html")
