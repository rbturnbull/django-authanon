from django.contrib.auth.models import Group
from django.contrib.auth.backends import BaseBackend
from django.conf import settings

def get_group_from_settings(key, default):
    group_name = getattr(settings, key, default)
    group, _ = Group.objects.get_or_create(name=group_name)
    return group

def get_anonymous_group():
    return get_group_from_settings("AUTHANON_ANONYMOUS_GROUP", "Anonymous")    

def get_login_group():
    return get_group_from_settings("AUTHANON_LOGIN_GROUP", "Login Users")    

class AuthanonBackend(BaseBackend):
    """ Adapted from https://stackoverflow.com/a/31520798 """
    perm_cache_name = '_authanon_perm_cache'
    
    def get_permissions_group_name(self, group):
        #largely from django.contrib.auth.backends
        perms = group.permissions.all()
        perms = perms.values_list('content_type__app_label', 'codename').order_by()
        perms = set("%s.%s" % (ct, name) for ct, name in perms)
        return perms

    def get_group_permissions(self, user_obj, obj=None):
        if not hasattr(user_obj, self.perm_cache_name):
            perms = self.get_permissions_group_name(get_anonymous_group())
            if not user_obj.is_anonymous:
                perms |= self.get_permissions_group_name(get_login_group())
            setattr(user_obj, self.perm_cache_name, perms)
        return getattr(user_obj, self.perm_cache_name)

    def get_all_permissions(self, user_obj, obj=None):
        return self.get_group_permissions(user_obj, obj)

    def has_perm(self, user_obj, perm, obj=None):
        return perm in self.get_all_permissions(user_obj, obj)

