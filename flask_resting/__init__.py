from flask import current_app, _app_ctx_stack, request
from ._errors import ResourceIsNotInherited as _ResourceIsNotInherited

class FlaskResting(object):
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.app = app
        try:
            app.teardown_appcontext(self.teardown)
        except:
            pass

    def teardown(self, exception):
        ctx = _app_ctx_stack.top

    def add_resource(self, resource, url, name=None, **kwargs):
        if resource is Resource:
            raise _ResourceIsNotInherited()

        resource = resource()

        def execute_view(*args, **kwargs):
            if request.method == 'GET':
                return resource.get(*args, **kwargs)
            elif request.method == 'POST':
                return resource.post(*args, **kwargs)
            elif request.method == 'PUT':
                return resource.put(*args, **kwargs)
            elif request.method == 'PATCH':
                return resource.patch(*args, **kwargs)
            elif request.method == 'DELETE':
                return resource.delete(*args, **kwargs)
            elif request.method == 'HEAD':
                return resource.head(*args, **kwargs)
            elif request.method == 'CONNECT':
                return resource.connect(*args, **kwargs)
            elif request.method == 'OPTIONS':
                return resource.options(*args, **kwargs)
            elif request.method == 'TRACE':
                return resource.trace(*args, **kwargs)
            else:
                return resource._method_not_allowed()

        with self.app.app_context():
            current_app.add_url_rule(
                url,
                name or url.__class__.__name__,
                execute_view,
                **kwargs
            )

class Resource(object):
    def __init__(self):
        pass

    def _method_not_allowed(self):
        return """
        <title>405 Method Not Allowed</title>
        <h1>Method Not Allowed</h1>
        <p>The method is not allowed for the requested URL.</p>
        """

    def get(self):
        return self._method_not_allowed()

    def post(self):
        return self._method_not_allowed()

    def put(self):
        return self._method_not_allowed()

    def patch(self):
        return self._method_not_allowed()

    def delete(self):
        return self._method_not_allowed()

    def head(self):
        return self._method_not_allowed()

    def connect(self):
        return self._method_not_allowed()

    def options(self):
        return self._method_not_allowed()

    def trace(self):
        return self._method_not_allowed()
