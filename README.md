# Social Network API — Flask & SQLAlchemy


This project defines a **data model** for a **social network** application, inspired by platforms such as Instagram, using **Flask** and **SQLAlchemy**.
It includes users, posts, comments, media files, and a follower system.

The example in Google Sheets for the tables is as follows:

![Set of 5 tables with data model information for an Instagram-type social network. It contains a table with user information, one for files, another for posts, another for comments, and a final one to establish the relationship between users who are followed and their followers](https://i.ibb.co/cSpmkrXc/Captura-de-pantalla-2026-01-11-085141.png “Instagram data model”).

The main objective is to **practice relationships between tables** (one-to-many and many-to-many).

---

## Technologies used

- Python
- Flask
- Flask-SQLAlchemy
- SQLAlchemy ORM

---

## Data model structure

The application consists of the following models:
- User
- Post
- Media
- Comment
- Follows

---

## Models and relationships

### 1. User

Represents users registered on the platform.
**Main fields:**

- `id`
- `user_name` (unique)
- `name`
- `last_name`
- `email` (unique)
- `password`
- `is_active`

**Relationships:**

A user can:
- Have many posts
- Write many comments
- Follow other users
- Be followed by other users

---

### 2. Post

Represents posts created by users.
**Main fields:**

- `id`
- `description`
- `user_id` (FK)

**Relationships:**

A post:
- Belongs to a user
- Can have many comments
- Can have many media files

---

### 3. Media

Represents the media files associated with a publication (image, video, etc.).
**Main fields:**

- `id`
- `type`
- `url`
- `post_id` (FK)

**Relationships:**
- Each media file belongs to a post
- If the same file is uploaded more than once, they will be treated as different

---

### 4. Comment

Represents comments that users make on posts.
**Main fields:**

- `id`
- `date`
- `text`
- `user_id` (FK)
- `post_id` (FK)

**Relationships:**

A comment:
- Belongs to a user
- Belongs to a post

---

### 5. Follows

Manages the relationship between users who follow and are followed.
This model allows us to represent a many-to-many relationship between users, including additional information such as the date of the follow.
**Main fields:**

- `id`
- `date`
- `follower_id` (FK to User)
- `followed_id` (FK to User)

**Relationships:**
A user can:
- Follow many users
- Be followed by many users

---

## Implemented relationships

- **One-to-many**
- User → Post
- User → Comment
- Post → Comment
- Post → Media
- **Many-to-many**
- User ↔ User (through `Follows`)
