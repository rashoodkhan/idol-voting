"""
Django settings for idolapp project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=0z8(peut_=b937c^5rp%!5-$x&x(fq@znzkke^m6v1y9g@uis'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'poll',
     'social.apps.django_app.default',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'idolapp.urls'

WSGI_APPLICATION = 'idolapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.mysql',
        'NAME': 'idol',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        #'PORT': '3306',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_CONTEXT_PROCESSORS = (
'django.contrib.auth.context_processors.auth',
'django.core.context_processors.debug',
'django.core.context_processors.i18n',
'django.core.context_processors.media',
'django.contrib.messages.context_processors.messages',
'social.apps.django_app.context_processors.backends',
)

#Django Social Auth
AUTHENTICATION_BACKENDS = (
'social.backends.amazon.AmazonOAuth2',
'social.backends.angel.AngelOAuth2',
'social.backends.aol.AOLOpenId',
'social.backends.appsfuel.AppsfuelOAuth2',
'social.backends.beats.BeatsOAuth2',
'social.backends.behance.BehanceOAuth2',
'social.backends.belgiumeid.BelgiumEIDOpenId',
'social.backends.bitbucket.BitbucketOAuth',
'social.backends.box.BoxOAuth2',
'social.backends.clef.ClefOAuth2',
'social.backends.coinbase.CoinbaseOAuth2',
'social.backends.coursera.CourseraOAuth2',
'social.backends.dailymotion.DailymotionOAuth2',
'social.backends.disqus.DisqusOAuth2',
'social.backends.douban.DoubanOAuth2',
'social.backends.dropbox.DropboxOAuth',
'social.backends.dropbox.DropboxOAuth2',
'social.backends.evernote.EvernoteSandboxOAuth',
'social.backends.facebook.FacebookAppOAuth2',
'social.backends.facebook.FacebookOAuth2',
'social.backends.fedora.FedoraOpenId',
'social.backends.fitbit.FitbitOAuth',
'social.backends.flickr.FlickrOAuth',
'social.backends.foursquare.FoursquareOAuth2',
'social.backends.github.GithubOAuth2',
'social.backends.google.GoogleOAuth',
'social.backends.google.GoogleOAuth2',
'social.backends.google.GoogleOpenId',
'social.backends.google.GooglePlusAuth',
'social.backends.google.GoogleOpenIdConnect',
'social.backends.instagram.InstagramOAuth2',
'social.backends.jawbone.JawboneOAuth2',
'social.backends.linkedin.LinkedinOAuth',
'social.backends.linkedin.LinkedinOAuth2',
'social.backends.live.LiveOAuth2',
'social.backends.livejournal.LiveJournalOpenId',
'social.backends.mailru.MailruOAuth2',
'social.backends.mendeley.MendeleyOAuth',
'social.backends.mendeley.MendeleyOAuth2',
'social.backends.mineid.MineIDOAuth2',
'social.backends.mixcloud.MixcloudOAuth2',
'social.backends.nationbuilder.NationBuilderOAuth2',
'social.backends.odnoklassniki.OdnoklassnikiOAuth2',
'social.backends.open_id.OpenIdAuth',
'social.backends.openstreetmap.OpenStreetMapOAuth',
'social.backends.persona.PersonaAuth',
'social.backends.podio.PodioOAuth2',
'social.backends.rdio.RdioOAuth1',
'social.backends.rdio.RdioOAuth2',
'social.backends.readability.ReadabilityOAuth',
'social.backends.reddit.RedditOAuth2',
'social.backends.runkeeper.RunKeeperOAuth2',
'social.backends.skyrock.SkyrockOAuth',
'social.backends.soundcloud.SoundcloudOAuth2',
'social.backends.spotify.SpotifyOAuth2',
'social.backends.stackoverflow.StackoverflowOAuth2',
'social.backends.steam.SteamOpenId',
'social.backends.stocktwits.StocktwitsOAuth2',
'social.backends.stripe.StripeOAuth2',
'social.backends.suse.OpenSUSEOpenId',
'social.backends.thisismyjam.ThisIsMyJamOAuth1',
'social.backends.trello.TrelloOAuth',
'social.backends.tripit.TripItOAuth',
'social.backends.tumblr.TumblrOAuth',
'social.backends.twilio.TwilioAuth',
'social.backends.twitter.TwitterOAuth',
'social.backends.vk.VKOAuth2',
'social.backends.weibo.WeiboOAuth2',
'social.backends.xing.XingOAuth',
'social.backends.yahoo.YahooOAuth',
'social.backends.yahoo.YahooOpenId',
'social.backends.yammer.YammerOAuth2',
'social.backends.yandex.YandexOAuth2',
'social.backends.vimeo.VimeoOAuth1',
'social.backends.lastfm.LastFmAuth',
'social.backends.moves.MovesOAuth2',
'social.backends.email.EmailAuth',
'social.backends.username.UsernameAuth',
'django.contrib.auth.backends.ModelBackend',
)


SOCIAL_AUTH_FACEBOOK_KEY = '513596625445095'
SOCIAL_AUTH_FACEBOOK_SECRET = 'f7f7e6524dcbd5c9f768c727667f1643'

LOGIN_URL = '/'
LOGIN_REDIRECT_URL = '/vote'
URL_PATH = ''
SOCIAL_AUTH_STRATEGY = 'social.strategies.django_strategy.DjangoStrategy'
SOCIAL_AUTH_STORAGE = 'social.apps.django_app.default.models.DjangoStorage'

PROJECT_APP_DIR = os.path.realpath(os.path.dirname(__file__))
PROJECT_DIR = os.path.dirname(PROJECT_APP_DIR)

MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')

MEDIA_URL = '/media/'

STATIC_ROOT = ''

STATIC_URL = '/static/'

SOCIAL_AUTH_PIPELINE = (
'social.pipeline.social_auth.social_details',
'social.pipeline.social_auth.social_uid',
'social.pipeline.social_auth.auth_allowed',
'social.pipeline.social_auth.social_user',
'social.pipeline.user.get_username',
'example.app.pipeline.require_email',
'social.pipeline.mail.mail_validation',
'social.pipeline.user.create_user',
'social.pipeline.social_auth.associate_user',
'social.pipeline.debug.debug',
'social.pipeline.social_auth.load_extra_data',
'social.pipeline.user.user_details',
'social.pipeline.debug.debug'
)


