# 🧠 RecuerdaMe

**RecuerdaMe** es una aplicación pensada para ayudar a personas con problemas de memoria, asistiendo en su día a día con recordatorios, organización y seguimiento de tareas importantes. El objetivo es mejorar su autonomía y calidad de vida mediante una herramienta sencilla y accesible.

---

## 🚀 Características principales

- Recordatorios personalizados.
- Organización diaria/semanal.
- Alertas sonoras y visuales para tareas urgentes.
- Filtros por tareas del día, próximas o sin realizar.
- Botón de revisión de lo que hizo ayer.
- Seguridad por niveles (personal, tutor y administrador).
- Relación con persona de seguimiento (tutor).
- Interfaz amigable y adaptada a personas con dificultades cognitivas.
- Base de datos persistente para mantener toda la información guardada.

---

## 🛠️ Tecnologías utilizadas

- **Python 3**
- **Django 5.2**
- **SQLite** para desarrollo local
- **PostgreSQL 16** para producción
- **Bootstrap 5** para diseño moderno y accesible
- HTML/CSS para la interfaz de usuario

---

## 🗂️ Estructura del proyecto

```
RecuerdaMe/
├── agenda/                    # App principal con vistas, modelos y formularios
├── config/                    # Configuración global del proyecto Django
├── templates/agenda/         # Plantillas HTML personalizadas
├── palabras_prohibidas.txt   # Palabras que se deben evitar en los textos
├── db.sqlite3                # Base de datos local
├── manage.py                 # Script principal de Django
```

---

!!!IMPORTANTE¡¡¡ Para evitar errores al editar código fuente, todos los archivos incluirán una línea al inicio indicando su ruta, por ejemplo:

```python
# agenda/views.py
```

---

## 🌐 Repositorio

GitHub: [https://github.com/GenX77/RecuerdaMe](https://github.com/GenX77/RecuerdaMe)

---

## 💡 Propósito social y reflexiones

Esta herramienta nació para ayudar a la hija de una amiga que sufrió un accidente de tráfico, lo que le provocó una lesión cerebral y pérdida de memoria a corto plazo.

### ¿Cómo ayuda RecuerdaMe?

- 🧠 **Memoria externa confiable**: puede ver lo que tiene que hacer y lo que hizo sin depender de su memoria.
- 😌 **Reducción de ansiedad**: evita frustraciones al olvidar cosas.
- 📚 **Apoyo para estudiar o trabajar**: con rutinas simples y recordatorios.
- 🔔 **Alertas visuales y sonoras**: mejoran su atención sin saturarla.
- 👥 **Seguimiento por parte de tutores**: permite a su tutor ver su progreso o dejarle sugerencias.
- 📅 **Resumen del día anterior**: acceso a lo que hizo ayer con un solo clic.
- 🎙️ **Notas de voz o fotos rápidas**: opción futura para mejorar accesibilidad.
- 🧠 **Ejercicios de memoria**: Sin que lo sepa el usuario, incluir ejercicios que le ayuden a ejercitar su memoria. 

---

## 🔒 Niveles de Seguridad

### Nivel 1: Usuario Principal
- Ve y gestiona sus propias tareas y notas.
- Clasifica información como pública, privada o íntima.

### Nivel 2: Tutor / Persona de Confianza
- Accede a tareas visibles marcadas como seguimiento.
- Puede recibir alertas de olvido.
- Puede escribir comentarios.

### Nivel 3: Administrador del Sistema (opcional)
- Manejo técnico del sistema.
- Sin acceso a datos personales.

### Accesos y Privacidad
- Público: accesible por usuario y tutor.
- Privado: solo para el usuario.
- Íntimo: requiere PIN adicional.

---

## 👤 Persona de Seguimiento
Modelo de perfil con relación a un tutor asignado.

- Permite que el tutor vea solo lo autorizado.
- Requiere autenticación del tutor.

---

## 🔐 Seguridad Extra

- Autenticación de dos pasos para datos sensibles.
- Cifrado en base de datos.
- Registros de auditoría para accesos y ediciones.