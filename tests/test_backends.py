from django.test import TestCase
from django.contrib.auth.models import Group
from django.test import Client
from django.urls import reverse
# from django.core.management import call_command
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import AnonymousUser, UserManager, User

from .models import TestAuthAnonModel
from authanon.backends import get_anonymous_group, get_login_group

class AuthanonBackendTests(TestCase):
    urls = 'tests.urls'

    def setUp(self):
        ct = ContentType.objects.get_for_model(TestAuthAnonModel)
        group = get_anonymous_group()
        group.permissions.add( 
            Permission.objects.get(codename='view_testauthanonmodel',content_type=ct)
        )
        group = get_login_group()
        group.permissions.add( 
            Permission.objects.get(codename='change_testauthanonmodel',content_type=ct),
        )

    def assert_status_code(self, client, url_name, status_code):
        response = client.get(reverse(url_name))
        self.assertEqual(response.status_code, status_code, f'Url: {url_name}')

    def test_anon(self):
        client = Client()
        self.assert_status_code( client, "home", 200 )
        self.assert_status_code( client, "private", 302 )
        self.assert_status_code( client, "secret", 302 )

    def test_login_user(self):
        client = Client()
        user = User.objects.create_user(username='fred', password='secret')
        client.force_login(user=user)
        self.assert_status_code( client, "home", 200 )
        self.assert_status_code( client, "private", 200 )
        self.assert_status_code( client, "secret", 403 )

    def test_super_user(self):
        client = Client()
        user = User.objects.create_superuser(username='super fred', password='secret')
        client.force_login(user=user)
        self.assert_status_code( client, "home", 200 )
        self.assert_status_code( client, "private", 200 )
        self.assert_status_code( client, "secret", 200 )
