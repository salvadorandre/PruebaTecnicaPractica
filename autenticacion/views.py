from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Tareas
# Create your views here.

# Funcion para realizar el registro de usuarios 
def registro(request):
    if(request.method == 'GET'): 
        return render(request, 'registrar.html')
    else: 
        #Crear un nuevo usuario 
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        #Verifica que el usuario y correo no existan
        if User.objects.filter(username=request.POST['username']).exists():
            return render(request, 'registrar.html', {'error': 'El nombre de usuario ya existe'})
        if User.objects.filter(email=request.POST['email']).exists():
            return render(request, 'registrar.html', {'error': 'El correo electrónico ya está en uso'})
        user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
        user.save()    
        return render(request, 'Tareas/inicio.html')
# Funcion para iniciar sesion    
def iniciarSesion(request):

    if(request.method == 'GET'):
        return render(request, 'login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, 'inicio.html')
        else:
            return render(request, 'login.html', {'error': 'Credenciales inválidas'})

#Funcion que retorna a la pagina de inicio
@login_required
def inicio(request):
    return render(request, 'inicio.html')

#Funcion para poder rehacer la contrasena del usuario
def recuperarContrasena(request):
    if(request.method == 'GET'):
        return render(request, 'recuperarContrasena.html')
    else:
        #Recuperar contrasena del usuario con el email que se de
        email = request.POST['email']
        try:
            user = User.objects.get(email=email)
            new_password = User.objects.make_random_password()
            user.set_password(new_password)
            user.save()
            # Enviar contrasena al corre en caso de que el correo exista 
            return render(request, 'login.html', {'success': f'Su nueva contraseña es: {new_password}'})
        except User.DoesNotExist:
            return render(request, 'recuperarContrasena.html', {'error': 'El correo electrónico no está registrado'})
#Cerrar sesion de la app
def cerrarSesion(request):
    logout(request)
    return render(request, 'login.html')

#Funcion para listar las tareas del usuario logeado

@login_required
def listarTareas(request): 

    tareas = Tareas.objects.filter(usuario=request.user)
    return render(request, 'listadoTareas.html', {'tareas': tareas})

#funcion para crear una nueva tarea 
@login_required
def crearTarea(request):
    if request.method == 'GET':
        return render(request, 'crearTarea.html')
    else:
        nombre = request.POST['nombre']
        fecha_vencimiento = request.POST['fecha_vencimiento']
        prioridad = request.POST['prioridad']
        estado = request.POST['estado']

        tarea = Tareas(
            nombre=nombre,
            fecha_vencimiento=fecha_vencimiento,
            prioridad=prioridad,
            estado=estado,
            usuario=request.user
        )
        tarea.save()
        return render(request, 'listadoTareas.html', {'success': 'Tarea creada'})
    
#Funcion para editar la tarea seleccionada y mostrar la informacion de la tarea
@login_required
def informacionTarea(request, idTarea): 

    if request.method == 'GET':
        tarea = get_object_or_404(Tareas, pk=idTarea)
        return render(request, 'editarTarea.html', {'tarea': tarea})
    else:
        tarea.nombre = request.POST['nombre']
        tarea.fecha_vencimiento = request.POST['fecha_vencimiento']
        tarea.prioridad = request.POST['prioridad']
        tarea.estado = request.POST['estado']
        tarea.save()
        return render(request, 'listadoTareas.html', {'success': 'Tarea actualizada'})


@login_required
def eliminarTarea(request, idTarea):
    tarea = get_object_or_404(Tareas, pk=idTarea)
    tarea.delete()
    return render(request, 'listadoTareas.html', {'success': 'Tarea eliminada'})