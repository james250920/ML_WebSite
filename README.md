# 🚀 ML Website

Aplicación Flask profesional con arquitectura modular, escalable y bien organizada.

> **Ver estructura detallada**: Consulta [`ESTRUCTURA.md`](ESTRUCTURA.md) para información completa sobre la organización del proyecto.

## ✨ Características

- 🏗️ **Arquitectura Modular**: Separación clara entre vistas, rutas y templates
- 📦 **Blueprints**: Organización por funcionalidad usando Flask Blueprints
- 🎨 **Templates Modernos**: Diseño responsive con HTML5 y CSS3
- 🔧 **Configuración por Ambiente**: Dev, Production y Testing
- 📝 **Bien Documentado**: Docstrings y comentarios en todo el código
- 🧪 **Fácil de Extender**: Estructura clara para agregar nuevas funcionalidades

## 📁 Estructura del Proyecto

```
ML_WEBSITE/
│
├── app.py                      # Archivo principal de la aplicación
├── requirements.txt            # Dependencias del proyecto
│
├── pages/                      # 📄 Vistas de la aplicación
│   ├── __init__.py
│   ├── landing/               # Vista de página principal
│   │   ├── __init__.py
│   │   ├── landingPage.py     # Blueprint de landing
│   │   └── landing.html       # Template (deprecated - usar templates/)
│   │
│   └── about/                 # Vista de página about
│       ├── __init__.py
│       ├── aboutPage.py       # Blueprint de about
│       └── about.html         # Template (deprecated - usar templates/)
│
├── router/                     # 🛣️ Rutas de la aplicación
│   ├── __init__.py
│   └── router.py              # Rutas API y funcionalidades generales
│
└── templates/                  # 🎨 Templates HTML
    ├── landing.html           # Template de página principal
    └── about.html             # Template de página about

```

## 🎯 Organización del Código

### `/pages` - Vistas
Contiene los blueprints de las vistas organizados en subcarpetas. Cada vista tiene su propio módulo.

**Ejemplo:**
- `pages/landing/landingPage.py` - Blueprint para la página principal
- `pages/about/aboutPage.py` - Blueprint para la página about

### `/router` - Rutas
Contiene las rutas de API y funcionalidades generales que no son vistas específicas.

**Ejemplo:**
- Rutas API (`/api/*`)
- Rutas con parámetros (`/user/<nombre>`)
- Endpoints de utilidad

### `/templates` - Templates HTML
Contiene todos los archivos HTML que usa `render_template()`.

## 🚀 Inicio Rápido

### Opción 1: Script Automático (Recomendado)
```powershell
.\start.ps1
```

### Opción 2: Manual
1. **Activar el entorno virtual:**
```powershell
.\venv\Scripts\Activate.ps1
```

2. **Instalar dependencias:**
```powershell
pip install -r requirements.txt
```

3. **Ejecutar la aplicación:**
```powershell
python app.py
```

4. **Abrir en el navegador:** `http://localhost:5000`

### Configurar Ambiente
```powershell
# Desarrollo (por defecto)
python app.py

# Producción
$env:FLASK_ENV="production"; python app.py

# Testing
$env:FLASK_ENV="testing"; python app.py
```

## 📝 Agregar Nuevas Vistas

1. Crear carpeta en `pages/nueva_vista/`
2. Crear `__init__.py` en la carpeta
3. Crear archivo Python con el blueprint (ej: `nuevaVistaPage.py`)
4. Crear template HTML en `templates/nueva_vista.html`
5. Registrar el blueprint en `app.py`

## 📝 Agregar Nuevas Rutas API

1. Abrir `router/router.py`
2. Agregar la nueva ruta al blueprint `main_routes`

## 🛠️ Tecnologías

- **Flask** - Framework web
- **Python 3.x** - Lenguaje de programación
- **HTML5/CSS3** - Frontend

## 📋 Rutas Disponibles

- `/` - Página principal (landing)
- `/about` - Acerca de la aplicación
- `/user/<nombre>` - Ejemplo con parámetros
- `/api/hello` - API de ejemplo (GET)
- `/api/datos` - API para recibir datos (POST)
