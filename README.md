## Aplicación CRUD Modular
## Sistema de Registro de Visitantes
## 🧾 1. Descripción General

El presente proyecto consiste en el desarrollo de una aplicación de escritorio utilizando Python y Tkinter, cuyo objetivo es gestionar el registro de visitantes dentro de una oficina.

El sistema permite realizar operaciones CRUD (agregar, limpiar, Actualizar y Eliminar) aplicando una arquitectura modular por capas, lo que facilita la organización, mantenimiento y escalabilidad del código.

##  2. Arquitectura del Sistema

El sistema está dividido en cuatro capas principales:
visitas_app/
│
├── main.py
├── modelos/
│   └── visitante.py
├── servicios/
│   └── visita_servicio.py
└── ui/
     └── app_tkinter.py

### 🔹 Modelos (`modelos/visitante.py`)

Contiene la clase `Visitante`, que representa la estructura de los datos:

* Cédula
* Nombre
* Motivo
Se aplican validaciones como:
* Cédula obligatoria de 10 dígitos
* Nombre no vacío
* Motivo no vacío

### 🔹 Servicios (`servicios/visita_servicio.py`)

Contiene la lógica del negocio:

* Registrar visitante
* Obtener lista de visitantes
* Actualizar visitante
* Eliminar visitante

Los datos se almacenan en memoria mediante una lista privada.

### 🔹 Interfaz Gráfica (`ui/app_tkinter.py`)

Desarrollada con Tkinter, permite la interacción del usuario.

Incluye:

* Formulario de entrada
* Botones de acción (Registrar, Actualizar, Eliminar, Limpiar)
* Tabla dinámica (Treeview)
* Validaciones visuales con messagebox

### 🔹 Main (`main.py`)

Archivo principal que inicia la aplicación:

* Crea el servicio
* Inyecta dependencia en la UI
* Ejecuta la aplicación

## ⚙️ 3. Funcionamiento del Sistema
### 🔸 Registro de Visitantes

El usuario ingresa los datos y presiona "Registrar":

* Se valida la información
* Se crea un objeto Visitante
* Se almacena en memoria
* Se actualiza la tabla

### 🔸 Visualización

Los visitantes registrados se muestran en una tabla dinámica que se actualiza automáticamente.

### 🔸 Actualización de Datos

* El usuario selecciona un registro de la tabla
* Puede modificar nombre, motivo o cédula
* Se actualiza el registro correctamente en memoria

### 🔸 Eliminación

* Se selecciona un registro
* Se solicita confirmación
* Se elimina el visitante de la lista

### 🔸 Limpieza de Campos

* Permite borrar los datos del formulario en un solo clic

## 🐞 5. Problemas Encontrados y Soluciones

Durante el desarrollo del sistema se identificaron varios errores:

### ❌ Error 1: No se eliminaban registros

**Causa:**
Se dependía de una variable de estado (`_cedula_seleccionada`) que no siempre tenía el valor correcto.

**Solución:**
Se obtuvo la cédula directamente desde la tabla seleccionada.

### ❌ Error 2: No se actualizaban los datos

**Causa:**
El sistema no encontraba el registro al actualizar debido a inconsistencias en la cédula.

**Solución:**
Se corrigió la lógica para usar la cédula real del registro seleccionado.

### ❌ Error 3: Problemas con cédulas que empiezan con 0

**Causa:**
La cédula era tratada como número, perdiendo ceros iniciales.

**Solución:**
Se manejó la cédula como string en todo el sistema.

### ❌ Error 4: No se podía editar la cédula

**Causa:**
El campo estaba bloqueado (`disabled`).

**Solución:**
Se implementó una variable (`_cedula_original`) para permitir edición y actualización correcta.

### ❌ Error 5: Error en limpieza de campos

**Causa:**
Uso incorrecto de `tk.EN` en lugar de `tk.END`.

**Solución:**
Corrección del método `delete()`.


## 🎨 6. Mejoras Implementadas

* Interfaz gráfica moderna y profesional
* Uso de colores corporativos
* Validaciones robustas
* Confirmaciones al eliminar
* Manejo correcto de datos sensibles (cédula)

## 🧠 7. Conclusión

El desarrollo de esta aplicación permitió aplicar conceptos clave como:

* Programación Orientada a Objetos (POO)
* Arquitectura modular
* Separación de responsabilidades
* Manejo de interfaces gráficas con Tkinter

El sistema cumple con todos los requisitos funcionales planteados y presenta una base sólida para futuras mejoras.

