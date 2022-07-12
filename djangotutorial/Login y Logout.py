'''

El parámetro "next=" indica a login o logout a donde redirigirse tras loguear.

-Add django.contrib.auth to INSTALLED APPS and urlpatterns
-Create a template named 'registration/login.htm'
-Get urls for login and logout using reverse, reversa_lazy or the url template tag.
-Add the "next=" parameter to those urls to bring the user back to a page after successful login or logout.
-Add LoginRequiredMixin to views that can only be accessed by a logged user. -> Clase en views.





'''