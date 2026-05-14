import dash
from django.http import HttpResponse


def create_dash_app():
    from charts.dash_setup import create_dash_app
    return create_dash_app(requests_pathname_prefix='/dash/')


def dashboard(request, path=''):
    app = create_dash_app()
    response = HttpResponse()

    def start_response(status, headers):
        response.status_code = int(status.split()[0])
        for header in headers:
            response[header[0]] = header[1]
        return lambda x: None

    environ = request.environ.copy()
    full_path = f'/{path}' if path else '/'
    environ['PATH_INFO'] = full_path
    environ['SCRIPT_NAME'] = '/dash'

    result = app.server(environ, start_response)

    for chunk in result:
        if chunk:
            response.write(chunk)

    return response