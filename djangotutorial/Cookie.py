# Esto va en views.py

def cookie(request):
    print(request.cookies)
    resp = HttpResponse('C is for cookie and that is good enough for me...')
    resp.set_cookie('zap',42) # No expired date = until browser close
    resp.set_cookie('sakaicar', 42, max_age=1000) # Seconds until expire
    return resp