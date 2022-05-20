# Copyright 2022 ITCase (info@itcase.pro)

# Django Grappelli
# https://github.com/sehmaschine/django-grappelli

# The Site Title of your admin interface.
GRAPPELLI_ADMIN_TITLE = 'ITCase Django Test Task'

# A dictionary containing search patterns for models you cannot (or should not)
# alter.
GRAPPELLI_AUTOCOMPLETE_SEARCH_FIELDS = {
    'auth': {
        'user': ('first_name__icontains', 'last_name__icontains',
                 'username__icontains', 'email__icontains'),
        'group': ('name__icontains', ),
    }
}

GRAPPELLI_INDEX_DASHBOARD = 'dashboard.ProjectDashboard'
