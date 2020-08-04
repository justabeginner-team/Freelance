from django.urls import path

from .views import (
    C2bConfirmation,
    C2bValidation,
    OnlineCheckoutCallback,
)

app_name = "mpesa"

urlpatterns = [
   
    path(
        "c2b/confirmation", C2bConfirmation.as_view(), name="c2b_confirmation"
    ),
    path("c2b/validate", C2bValidation.as_view(), name="c2b_validation"),
    path(
        "c2b/online_checkout/callback",
        OnlineCheckoutCallback.as_view(),
        name="c2b_checkout_callback",
    ),
]
