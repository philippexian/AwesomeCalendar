from flask_oauthlib.client import OAuth
from app import app


class authenfication:
    def __init__(self, type):
        self.type = type
        self.oauth = self.Get_OAuth()

    def Get_OAuth(self):
        oauthrequest = OAuth(app)
        if self.type == 'google':

            oauth = oauthrequest.remote_app(
                'google',
                consumer_key=app.config['GOOGLE_ID'],
                consumer_secret=app.config['GOOGLE_SECRET'],
                request_token_params={
                    'scope': 'https://www.googleapis.com/auth/calendar.readonly https://www.googleapis.com/auth/userinfo.email https://www.googleapis.com/auth/plus.login'  # noqa, needs to be cleaned
                },
                base_url='https://www.googleapis.com/oauth2/v1/',
                request_token_url=None,
                access_token_method='POST',
                access_token_url='https://accounts.google.com/o/oauth2/token',
                authorize_url='https://accounts.google.com/o/oauth2/auth',
            )
            return oauth
        elif self.type == 'facebook':
            oauth = oauthrequest.remote_app(
                'facebook',
                consumer_key=FACEBOOK_ID,
                consumer_secret=FACEBOOK_SECRET,
                request_token_params={
                    'scope': 'email, public_profile, user_about_me, user_relationships, user_events'
                },
                base_url='https://graph.facebook.com/',
                request_token_url=None,
                access_token_method='POST',
                access_token_url='/oauth/access_token',
                authorize_url='https://www.facebook.com/dialog/oauth',
            )
            return oauth
        return None


