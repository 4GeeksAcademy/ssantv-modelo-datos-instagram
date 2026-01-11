# API de Red Social — Flask & SQLAlchemy


Este proyecto define un **modelo de datos** para una aplicación de tipo **red social**, inspirada en plataformas como Instagram, utilizando **Flask** y **SQLAlchemy**.  
Incluye usuarios, publicaciones, comentarios, archivos multimedia y un sistema de seguidores.

El ejemplo en Google Sheets de las tablas es el siguiente:

![Conjunto de 5 tablas con la información del modelos de datos para una red social tipo Instagram. Contiene una tabla con la información de usuario, una para los archivos, otra para los post, otra para los comentarios y una última para hacer la relación entre usuarios seguidos y sus seguidores](https://i.ibb.co/cSpmkrXc/Captura-de-pantalla-2026-01-11-085141.png "Modelo de datos Instagram")

El objetivo principal es **practicar relaciones entre tablas** (uno a muchos y muchos a muchos).

---

## Tecnologías utilizadas

- Python
- Flask
- Flask-SQLAlchemy
- SQLAlchemy ORM

---

## Estructura del modelo de datos

La aplicación se compone de los siguientes modelos:

- User
- Post
- Media
- Comment
- Follows

---

## Modelos y relaciones

### 1. User (Usuario)

Representa a los usuarios registrados en la plataforma.

**Campos principales:**
- `id`
- `user_name` (único)
- `name`
- `last_name`
- `email` (único)
- `password`
- `is_active`

**Relaciones:**
- Un usuario puede:
  - Tener muchos posts
  - Escribir muchos comentarios
  - Seguir a otros usuarios
  - Ser seguido por otros usuarios

---

### 2. Post (Publicación)

Representa las publicaciones creadas por los usuarios.

**Campos principales:**
- `id`
- `description`
- `user_id` (FK)

**Relaciones:**
- Un post:
  - Pertenece a un usuario
  - Puede tener muchos comentarios
  - Puede tener muchos archivos multimedia

---

### 3. Media (Multimedia)

Representa los archivos multimedia asociados a una publicación (imagen, vídeo, etc.).

**Campos principales:**
- `id`
- `type`
- `url`
- `post_id` (FK)

**Relaciones:**
- Cada archivo multimedia pertenece a un post
- Se considera que si se sube un mismo archivo más de una vez, serán tratados como diferentes

---

### 4. Comment (Comentario)

Representa los comentarios que los usuarios realizan en las publicaciones.

**Campos principales:**
- `id`
- `date`
- `text`
- `user_id` (FK)
- `post_id` (FK)

**Relaciones:**
- Un comentario:
  - Pertenece a un usuario
  - Pertenece a un post

---

### 5. Follows (Seguidores)

Gestiona la relación de seguidores y seguidos entre usuarios.

Este modelo permite representar una relación **muchos a muchos** entre usuarios, incluyendo información adicional como la fecha del seguimiento.

**Campos principales:**
- `id`
- `date`
- `follower_id` (FK a User)
- `followed_id` (FK a User)

**Relaciones:**
- Un usuario puede:
  - Seguir a muchos usuarios
  - Ser seguido por muchos usuarios

---

## Relaciones implementadas

- **Uno a muchos**
  - User → Post
  - User → Comment
  - Post → Comment
  - Post → Media

- **Muchos a muchos**
  - User ↔ User (a través de `Follows`)
