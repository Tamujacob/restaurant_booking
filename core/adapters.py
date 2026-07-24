from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.contrib.auth.models import User


class CafeJavasSocialAccountAdapter(DefaultSocialAccountAdapter):

    def pre_social_login(self, request, sociallogin):
        """
        If a user with this email already exists (e.g. signed up normally
        with username/password), connect this Google login to that
        existing account instead of creating a duplicate.
        """
        email = sociallogin.account.extra_data.get('email')
        if not email:
            return

        if sociallogin.is_existing:
            return

        try:
            existing_user = User.objects.get(email=email)
            sociallogin.connect(request, existing_user)
        except User.DoesNotExist:
            pass

    def populate_user(self, request, sociallogin, data):
        """
        Auto-generate a username from the email so the manual
        signup-confirmation form is never shown to the user.
        """
        user = super().populate_user(request, sociallogin, data)
        email = data.get('email')

        if email:
            base_username = email.split('@')[0]
            username = base_username
            counter = 1
            while User.objects.filter(username=username).exists():
                username = f"{base_username}{counter}"
                counter += 1
            user.username = username

        return user