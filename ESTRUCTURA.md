# Estructura del Proyecto ML_WEBSITE

## 📂 Árbol de Directorios

```
ML_WEBSITE/
│
├── 📄 app.py                           # Aplicación principal (Factory Pattern)
├── 📄 config.py                        # Configuraciones (Dev, Prod, Test)
├── 📄 requirements.txt                 # Dependencias Python
├── 📄 README.md                        # Documentación del proyecto
├── 📄 .gitignore                       # Archivos ignorados por Git
├── 📄 start.ps1                        # Script de inicio rápido
│
├── 📁 pages/                           # VISTAS DE LA APLICACIÓN
│   ├── __init__.py                     # Inicializador del paquete
│   │
│   ├── 📁 landing/                     # Módulo Landing Page
│   │   ├── __init__.py
│   │   └── landingPage.py             # Blueprint: Ruta "/"
│   │
│   └── 📁 about/                       # Módulo About Page
│       ├── __init__.py
│       └── aboutPage.py               # Blueprint: Ruta "/about"
│
├── 📁 router/                          # RUTAS Y APIs
│   ├── __init__.py                     # Inicializador del paquete
│   └── router.py                      # Rutas API y generales
│                                       # - /user/<nombre>
│                                       # - /api/hello
│                                       # - /api/datos [POST]
│
├── 📁 templates/                       # TEMPLATES HTML
│   ├── landing.html                    # Template página principal
│   └── about.html                      # Template página about
│
├── 📁 venv/                            # Entorno virtual Python (ignorado)
├── 📁 __pycache__/                     # Cache Python (ignorado)
└── 📁 .git/                            # Repositorio Git

```

## 🎯 Convenciones y Organización

### 1. **Carpeta `pages/`** - Vistas/Páginas
- **Propósito**: Contiene blueprints de páginas/vistas completas
- **Estructura**: Cada vista tiene su propia carpeta
- **Contenido**: 
  - Archivo Python con el blueprint
  - `__init__.py` para hacer la carpeta un paquete
- **Ejemplo**: `pages/landing/landingPage.py`

### 2. **Carpeta `router/`** - Rutas API y Funcionales
- **Propósito**: Rutas que NO son vistas (APIs, endpoints, etc.)
- **Contenido**:
  - APIs REST
  - Rutas con parámetros dinámicos
  - Endpoints de utilidad
  - Webhooks
- **Ejemplo**: `/api/hello`, `/user/<nombre>`

### 3. **Carpeta `templates/`** - Templates HTML
- **Propósito**: Todos los archivos HTML para `render_template()`
- **Ubicación**: Flask busca templates aquí por defecto
- **Organización**: Planos o por subcarpetas según complejidad

### 4. **Archivos Raíz**
- **`app.py`**: Factory pattern, inicializa Flask y registra blueprints
- **`config.py`**: Configuraciones por ambiente
- **`requirements.txt`**: Dependencias del proyecto
- **`README.md`**: Documentación general
- **`start.ps1`**: Script para iniciar el proyecto fácilmente

## 📋 Flujo de una Petición

```
1. Cliente hace request → http://localhost:5000/about

2. Flask recibe en app.py

3. Busca en blueprints registrados
   ├── landing_page → No match
   ├── about_page → ✓ Match! (/about)
   └── main_routes → No match

4. Ejecuta about_page.about()

5. render_template('about.html')

6. Busca en templates/about.html

7. Renderiza y envía respuesta al cliente
```

## 🔄 Agregar Nuevas Funcionalidades

### ➕ Nueva Vista (Página):
```
1. Crear carpeta: pages/nueva_vista/
2. Crear: pages/nueva_vista/__init__.py
3. Crear: pages/nueva_vista/nuevaVistaPage.py
4. Crear: templates/nueva_vista.html
5. Registrar en app.py: app.register_blueprint(nueva_vista)
```

### ➕ Nueva Ruta API:
```
1. Abrir: router/router.py
2. Agregar decorador y función:
   @main_routes.route('/api/nueva')
   def nueva_api():
       return jsonify({'data': 'valor'})
```

### ➕ Nueva Configuración:
```
1. Abrir: config.py
2. Agregar en la clase Config apropiada
3. Usar en app: app.config['MI_CONFIG']
```

## 🎨 Estándares de Código

- **Docstrings**: Todos los módulos, clases y funciones
- **Type hints**: Usar cuando sea posible
- **PEP 8**: Seguir convenciones de Python
- **Comentarios**: Explicar el "por qué", no el "qué"
- **Nombres**: Descriptivos y en español/inglés consistente

## 🚀 Comandos Útiles

```powershell
# Activar entorno virtual
.\venv\Scripts\Activate.ps1

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar aplicación (opción 1)
python app.py

# Ejecutar aplicación (opción 2 - script)
.\start.ps1

# Actualizar requirements.txt
pip freeze > requirements.txt

# Modo producción
$env:FLASK_ENV="production"; python app.py
```

## 📝 Notas Importantes

1. **Templates**: Usar siempre `templates/` en la raíz, no en subcarpetas de pages
2. **Blueprints**: Cada vista = 1 blueprint, cada blueprint en su carpeta
3. **Router**: Solo para rutas que NO renderizan páginas completas
4. **Config**: Nunca hacer commit de secretos, usar variables de entorno
5. **Git**: El `.gitignore` ya está configurado correctamente
