from functools import wraps
from flask import request, render_template


def templated(template=None):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            print(f"template_name : {template}")
            template_name = template
            if template_name is None:
                template_name = f"{request.endpoint.replace('.', '/')}.html"
            ctx = f(*args, **kwargs)
            if ctx is None:
                ctx = {}
            elif not isinstance(ctx, dict):
                return ctx
            return render_template(template_name, **ctx)
        return decorated_function
    return decorator
