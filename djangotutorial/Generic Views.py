# -------------------------- Generic Views ----------------------- #

from django.views import generic
# importar models?
class HorseList(View):
    model = Horse
    def get(self, request):

        modelname= self.model._meta.verbose_name.title().lower() # Nombre del modelo en minúsculas
        stuff = model.objects.all()
        ctx = { modelname+'_list': stuff}
        return render(request, 'vista', ctx)

class HordeListView(generic.ListView):
    model = Horse

class DJ4EListView(View):
    def get(self, request):
        modelname = self.model._meta.verbose_name.title().lower()  # Nombre del modelo en minúsculas
        stuff = model.objects.all()
        ctx = {modelname + '_list': stuff}
        return render(request, 'vista', ctx)

# Reusar esta:

class CarListView(DJ4EListView):
    model = Car