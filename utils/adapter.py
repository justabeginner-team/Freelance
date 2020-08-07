from allauth.account.adapter import DefaultAccountAdapter


class ShopAdapter(DefaultAccountAdapter):
        def is_open_for_signup(self, request):
                """
                Checks whether or not the site is open for signups.

                Next to simply returning True/False you can also intervene the
                regular flow by raising an ImmediateHttpResponse
                """
                return True
