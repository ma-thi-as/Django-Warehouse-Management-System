# Django Warehouse Management System

Un sistema completo de gestión de bodega desarrollado con Django, que incluye generación de reportes PDF, control de inventario, y gestión de personal.

## 🚀 Características Principales

- **Gestión de Empleados**
  - Control de personal y roles
  - Registro de horarios y turnos
  - Asignación de tareas y responsabilidades

- **Gestión de Inventario**
  - Control de stock en tiempo real
  - Registro de entradas y salidas
  - Alertas de stock bajo
  - Histórico de movimientos
  - Códigos de barras/QR

- **Gestión de Proveedores**
  - Catálogo de proveedores
  - Historial de compras
  - Evaluación de proveedores
  - Gestión de órdenes de compra

- **Gestión del Área de Bodega**
  - Organización de espacios
  - Control de ubicaciones
  - Optimización de almacenamiento

- **Generación de PDF**
  - Reportes de inventario

## 📋 Requisitos Previos

```
Python 3.8+
Django 4.0+
PostgreSQL
virtualenv (recomendado)
```

## 🛠️ Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/your-username/django-warehouse.git
cd django-warehouse
```

2. Crear y activar entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Configurar variables de entorno:
```bash
cp .env.example .env
# Editar .env con tus configuraciones
```

5. Realizar migraciones:
```bash
python manage.py migrate
```

6. Crear superusuario:
```bash
python manage.py createsuperuser
```

7. Ejecutar servidor de desarrollo:
```bash
python manage.py runserver
```




![image](https://user-images.githubusercontent.com/116565550/205444619-73c72dae-64de-4ad7-aba3-958db79efd99.png)



![image](https://user-images.githubusercontent.com/116565550/205444744-c572e4bf-63f5-4eea-aaeb-177353fd1fb3.png)



![image](https://user-images.githubusercontent.com/116565550/205444766-7b871308-6dfc-4d0d-9809-4cb80a9fb54d.png)

![image](https://user-images.githubusercontent.com/116565550/205444830-c77e27b1-4882-4062-b12c-0b4b16540daa.png)

![image](https://user-images.githubusercontent.com/116565550/205444841-f1689cb2-0c71-43ea-b0e7-e2b95f1bd8f4.png)
