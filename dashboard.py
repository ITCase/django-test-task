# Copyright 2022 ITCase (info@itcase.pro)

# Django Grappelli Dashboard
# https://django-grappelli.readthedocs.io/en/latest/dashboard_setup.html

from django.urls import reverse_lazy

from grappelli.dashboard import modules, Dashboard


class ProjectDashboard(Dashboard):

    def init_with_context(self, context):

        request = context['request']

        management_models = ('django.contrib.*', 'rest_framework.authtoken.*')

        self.children.append(
            modules.AppList(title='Управление сайтом',
                            collapsible=True,
                            css_classes=['grp-closed'],
                            column=1,
                            models=management_models))
        self.children.append(
            modules.AppList(title='Приложения',
                            collapsible=True,
                            column=1,
                            exclude=management_models))

        if request.user.is_superuser:
            self.children.append(self.get_site_part())

        self.children.append(
            modules.LinkList(
                title='Управление файлами',
                collapsible=False,
                column=2,
                children=[{
                    'title': 'Менеджер файлов',
                    'url': reverse_lazy('filebrowser:fb_browse',
                                        current_app='filebrowser'),
                }],
            ))

        self.children.append(
            modules.RecentActions('Последние действия',
                                  limit=5,
                                  collapsible=False,
                                  column=2))

    def get_site_part(self):
        children = [{'title': 'Django RQ', 'url': reverse_lazy('rq_home')}]
        return modules.LinkList(title='Cайт',
                                collapsible=False,
                                column=2,
                                children=children)
