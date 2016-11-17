from pylons import config

import ckan.lib.helpers as h
import ckan.authz as authz
import ckan.plugins as p

from ckan.common import _, c, request
from ckan.controllers.user import UserController

class CustomUserController(UserController):
    def logged_in(self):
        # redirect if needed
        came_from = request.params.get('came_from', '')
        if h.url_is_local(came_from) and '/user/edit/' not in str(came_from):
            return p.toolkit.redirect_to(str(came_from))

        if c.user:
            context = None
            data_dict = {'id': c.user}

            user_dict = p.toolkit.get_action('user_show')(context, data_dict)

            if not c.user:
                h.redirect_to(locale=None, controller='user', action='login',
                              id=None)
            user_ref = c.userobj.get_reference_preferred_for_uri()

            if authz.is_sysadmin(c.user):
                p.toolkit.redirect_to(controller='package', action='search')

            org_list = p.toolkit.get_action('organization_list')({}, {})
            for org in org_list:
                if authz.has_user_permission_for_group_or_org(org, c.user, 'admin'):
                    p.toolkit.redirect_to(controller='organization', action='read', id=org)

                if authz.users_role_for_group_or_org(org, c.user) in ['editor','member']:
                    p.toolkit.redirect_to(controller='organization', action='read', id=org)

            p.toolkit.redirect_to(controller='user', action='dashboard')
        else:
            err = _('Login failed. Bad username or password.')
            if h.asbool(config.get('ckan.legacy_templates', 'false')):
                h.flash_error(err)
                h.redirect_to(controller='user', action='login', came_from=came_from)
            else:
                return self.login(error=err)