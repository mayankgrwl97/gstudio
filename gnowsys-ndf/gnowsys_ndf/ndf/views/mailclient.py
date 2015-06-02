# from django.views.generic import TemplateView
from django.shortcuts import render

# from gnowsys_ndf.settings import META_TYPE, GAPPS, GSTUDIO_SITE_DEFAULT_LANGUAGE, GSTUDIO_SITE_NAME
# from gnowsys_ndf.settings import GSTUDIO_RESOURCES_CREATION_RATING,
# GSTUDIO_RESOURCES_REGISTRATION_RATING, GSTUDIO_RESOURCES_REPLY_RATING

from gnowsys_ndf.ndf.models import *
from gnowsys_ndf.ndf.models import node_collection, triple_collection, gridfs_collection
# from gnowsys_ndf.ndf.models import *
from django.contrib.auth.models import User

from gnowsys_ndf.ndf.views.methods import get_drawers, get_execution_time
# from gnowsys_ndf.ndf.views.methods import create_grelation, create_gattribute
from gnowsys_ndf.ndf.views.methods import get_user_group, get_user_task, get_user_notification, get_user_activity, get_execution_time

from gnowsys_ndf.ndf.views.file import *
# from gnowsys_ndf.ndf.views.forum import *
from gnowsys_ndf.ndf.views.ajax_views import set_drawer_widget
# from gnowsys_ndf.notification import models as notification
from gnowsys_ndf.ndf.templatetags.ndf_tags import get_all_user_groups


@login_required
def mailclient(request, group_id):
    group_name, group_id = get_group_name_id(group_id)
    home_grp_id = node_collection.one({'name': "home"})

    if group_id == home_grp_id['_id']:
        return render(request, 'ndf/oops.html')

    return render(request, 'ndf/mailclient.html', {
        'groupname': group_name,
        'groupid': group_id
    })

# , mailbox_id=None, mailbox=None, count=0


# group_id necessary to pass because the templates require this
@login_required
@get_execution_time
def mailbox_create_edit(request, group_id):
	group_name, group_id = get_group_name_id(group_id)
	home_grp_id = node_collection.one({'name': "home"})
    
	if group_id == home_grp_id['_id']:
		return render(request, 'ndf/oops.html')
	template = "ndf/mailbox_create_edit.html"
	title = "Add A New Mailbox"
    
	variable = RequestContext(request, {'title': title,
    	'groupname': group_name,
        'groupid': group_id
        })
	return render_to_response(template, variable)
