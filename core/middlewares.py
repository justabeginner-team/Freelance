from django.contrib.sessions.models import Session


# helps us alter request and response
# so for every user checks if logged in
# if true delete previous session key and assign a new one
# else create a new session key


# this prevents a user from logging in with multiple sessions in play
class OneSessionPerUser:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        if request.user.is_authenticated:
            current_session_key = request.user.logged_in_user.session_key

            if current_session_key and current_session_key != request.session.session_key:
                Session.objects.get(session_key=current_session_key).delete()

            request.user.logged_in_user.session_key = request.session.session_key
            request.user.logged_in_user.save()

        response = self.get_response(request)
        # Code to be executed for each request/response after
        # the view is called.
        return response
