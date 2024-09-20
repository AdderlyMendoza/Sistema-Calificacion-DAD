import eel

# Inicializa Eel apuntando al directorio 'web'
eel.init('web')

# Exponer función de Python para ser llamada desde JavaScript
@eel.expose
def saludo_desde_python(nombre):
    print(f"HOLA, {nombre} desde Python!")  # Mensaje más claro

# Iniciar la aplicación y abrir el archivo 'index.html'
eel.start('index.html', size=(400, 300))  # Ajustar el tamaño de la ventana
