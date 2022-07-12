#import os
import django #Seguir este orden para que no de error de aplicación
django.setup()
from RagnarokDatabase.models import Kills, MVP
from django.contrib.auth.models import User
#from django.core.wsgi import get_wsgi_application

#application = get_wsgi_application()

#os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"


#u = User(name='Chimpancé Inalámbrico', password='barberay2')
#obj = User.objects.filter(name='Chimpancé Inalámbrico').exists() #Chequea si un objeto existe
#print(obj)

#obj2 = User.objects.get(name='Chimpancé Inalámbrico') # Aquí seleccionamos un objeto
#print(obj2.name, obj2.id, obj2.password) # Aquí mostramos sus parámetros

#Está la opción delete y otras.
#print(u.name)
#print(u.password)

# Checking -----------------------#

from django.db import connection
print(connection.queries)

#obj3 = Kills.objects.all()
#print(obj3)
obj3 = Kills.objects.filter().delete()
#print(MVP.objects.values())
print(User.objects.values())