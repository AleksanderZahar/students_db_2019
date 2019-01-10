# from settings import PORTAL_URL


def students_proc(request):
    # print request
    # print "HOST:", request.META['HTTP_HOST']
    portal = request.META['wsgi.url_scheme'] + '://' + request.META['HTTP_HOST']
    # portal = request.META['wsgi.url_scheme'] + '://' + request.META['SERVER_NAME'] + ':' + request.META['SERVER_PORT']
    # print "portal_url: ", portal
    return {'PORTAL_URL': portal}
    # return {'PORTAL_URL': request.META['HTTP_HOST']}
