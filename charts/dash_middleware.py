import os
from django.conf import settings
from dash import Dash
from django.urls import path


class DashRouter:
    def __init__(self):
        self.apps = {}

    def register(self, name, dash_app, url_path):
        self.apps[name] = {'app': dash_app, 'url': url_path}

    def get_urls(self):
        urls = []
        for name, data in self.apps.items():
            url_path = data['url']
            dash_app = data['app']
            urls.append(path(f'{url_path}', self.dash_view, kwargs={'app_name': name}))
            urls.append(path(f'{url_path}<path:path>', self.dash_view, kwargs={'app_name': name}))
        return urls

    def dash_view(self, request, app_name, path=''):
        if app_name in self.apps:
            dash_app = self.apps[app_name]['app']
            return dash_app.index()


dash_router = DashRouter()


def create_dash_app(url_path='dash/'):
    from charts.dash_setup import create_dash_app as make_dash_app
    app = make_dash_app(requests_pathname_prefix=f'/{url_path}')
    return app