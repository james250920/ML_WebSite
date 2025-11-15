# Script de inicio para desarrollo - ML Website
# Activa el entorno virtual y ejecuta la aplicación

Write-Host "🚀 Iniciando ML Website..." -ForegroundColor Cyan
Write-Host ""

# Activar entorno virtual si existe
if (Test-Path ".\venv\Scripts\Activate.ps1") {
    Write-Host "✓ Activando entorno virtual..." -ForegroundColor Green
    & .\venv\Scripts\Activate.ps1
} else {
    Write-Host "⚠ No se encontró el entorno virtual" -ForegroundColor Yellow
    Write-Host "  Ejecuta: python -m venv venv" -ForegroundColor Yellow
    exit
}

# Verificar dependencias
Write-Host "✓ Verificando dependencias..." -ForegroundColor Green
$flaskInstalled = pip list | Select-String "Flask"
if (-not $flaskInstalled) {
    Write-Host "⚠ Instalando dependencias..." -ForegroundColor Yellow
    pip install -r requirements.txt
}

Write-Host ""
Write-Host "✓ Iniciando aplicación Flask..." -ForegroundColor Green
Write-Host "  URL: http://localhost:5000" -ForegroundColor Cyan
Write-Host "  Presiona Ctrl+C para detener" -ForegroundColor Yellow
Write-Host ""

# Ejecutar aplicación
python app.py
