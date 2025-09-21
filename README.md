# 📦 Sistema de Inventario en Django  
**Evaluación N°2 – Programación Back End**  
Alumno: *Boris Saldaño*  

---

## 🚀 Requisitos Previos  
Antes de ejecutar el proyecto, asegúrate de tener instalado:  

- **Python 3.12+**  
- **Django 5.x**  
- **WAMP Server (con MySQL y phpMyAdmin)**  

Instalar dependencias necesarias:  

```bash
pip install django mysqlclient
```

---

## ⚙️ Configuración de la Base de Datos  
En phpMyAdmin, se utiliza la base de datos:  

- **Nombre:** inventariodb  
- **Usuario:** root 
- **Contraseña:** 1234  

En `settings.py` se configura la conexión:  

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'inventariodb',
        'USER': 'django',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

Aplicar migraciones:  

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 🛠️ Modelos Implementados  
La aplicación **inventario** contiene los siguientes modelos principales:  

- **Categoria** → Clasifica los productos.  
- **Proveedor** → Registro de proveedores.  
- **Bodega** → Lugares de almacenamiento.  
- **Producto** → Incluye nombre, categoría, proveedor, bodega y stock actual.  
- **Movimiento** → Registra operaciones de entrada, salida y merma.  

### Relaciones principales:  
- Un producto pertenece a una categoría y a un proveedor.  
- Un movimiento afecta al stock de un producto y está asociado a una bodega.  

### Reglas de stock:  
- **Entrada**: suma al stock.  
- **Salida** y **Merma**: restan stock (sin permitir valores negativos).  
- Todos los movimientos quedan registrados para ver el histórico por producto.  

---

## 🖥️ Uso del Administrador de Django  
Crear superusuario:  

```bash
python manage.py createsuperuser
```

Acceder al panel:  

👉 [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)  

Desde el admin se puede gestionar completamente:  

- Categorías  
- Proveedores  
- Bodegas  
- Productos  
- Movimientos  

Además, se personalizó el modelo **Producto** con:  

- `list_display` → mostrar columnas adicionales  
- `search_fields` → búsqueda por nombre o SKU  
- `list_filter` → filtrar por categoría y proveedor  

---

## 📄 Funcionalidades Disponibles  
- CRUD completo de los modelos desde el admin de Django.  
- Registro y control de movimientos con reglas de stock.  
- Visualización del histórico de movimientos por producto.  
- Templates básicos para ver listas, crear y editar registros.  

---

## ⚡ Cómo usar el proyecto paso a paso  

1. **Iniciar WAMP**  
   - Abrir WAMP y verificar que el icono esté verde.  
   - Acceder a phpMyAdmin en [http://localhost/phpmyadmin](http://localhost/phpmyadmin) y confirmar que existe la base `inventariodb`.  

2. **Configurar Django**  
   - Revisar `settings.py` y asegurarse que la base de datos y usuario coinciden.  

3. **Aplicar migraciones**  
   ```bash
   python manage.py makemigrations inventario
   python manage.py migrate
   ```

4. **Crear superusuario**  
   ```bash
   python manage.py createsuperuser
   ```

5. **Levantar servidor de desarrollo**  
   ```bash
   python manage.py runserver
   ```

6. **Acceder al admin**  
   - Ir a [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) e iniciar sesión.  

7. **Usar el CRUD**  
   - Crear, listar, editar y eliminar categorías, proveedores, bodegas y productos.  
   - Registrar movimientos (**entrada, salida, merma**) y verificar cómo afecta el stock.  
   - Usar los templates para interactuar con los datos.  
