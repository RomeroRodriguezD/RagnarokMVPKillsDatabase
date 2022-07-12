from django.views import View
from django.urls import reverse, reverse_lazy
from django.shortcuts import render

# EJEMPLO DE REVERSING URL, url de otras aplicaciones, aplicado a html templates

class Invent(View):
    def get(self, request):
        u = reverse_lazy('aplicación_ajena:nombre_vista_ajena')
        u2 = reverse('aplicación_ajena:nombre_vista_ajena', args=['valor'])
        ctx = {'x1':u, 'x2':u2}
        return render(request, 'ruta/*.html', ctx)

# En urls.py:
# path('camino', views.Invent.as_view(), name='invent-view')

