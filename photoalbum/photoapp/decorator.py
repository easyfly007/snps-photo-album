from django.http import HttpResponse, HttpResponseRedirect

def decorate(func):
    def validcheck(Request, *args, **kwargs):
        valid_user = Request.session.get('valid_user', False)
        if not valid_user:
            return HttpResponseRedirect('/login')
        return func(Request, *args, **kwargs)
    return validcheck