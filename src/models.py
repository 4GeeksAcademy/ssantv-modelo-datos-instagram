from __future__ import annotations
from typing import List

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)

    # Es padre de:
    posts: Mapped[List["Post"]] = relationship(back_populates="user")
    comments: Mapped[List["Comment"]] = relationship(back_populates="user")
    followers: Mapped[List["Follows"]] = relationship(foreign_keys="Follows.followed_id", back_populates="followed_user")
    following: Mapped[List["Follows"]] = relationship(foreign_keys="Follows.follower_id", back_populates="follower_user")
    
    # Añadir FK foreign_keys="a followers y following"
    def serialize(self):
        return {
            "id": self.id,
            "user_name": self.user_name,
            "name": self.name,
            "last_name": self.last_name,
            "password": self.password,
            "email": self.email,
            "is_active": self.is_active,
        }


class Post(db.Model):
    __tablename__ = "post"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    description: Mapped[str] = mapped_column(String(120), nullable=False)

    # Hijo de:
    user: Mapped["User"] = relationship(back_populates="posts")

    # Padre de:
    medias: Mapped[List["Media"]] = relationship(back_populates="post")
    comments: Mapped[List["Comment"]] = relationship(back_populates="post")

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "description": self.description
        }

class Media(db.Model):
    __tablename__ = "media"
    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str] = mapped_column(nullable=False)
    url: Mapped[str] = mapped_column(nullable=False)
    post_id: Mapped[int] = mapped_column(ForeignKey("post.id"))

    # Padre de:
    post: Mapped["Post"] = relationship(back_populates="medias")

    def serialize(self):
        return {
            "id": self.id,
            "type": self.type,
            "url": self.url,
            "post_id": self.post_id
        }


class Comment(db.Model):
    __tablename__ = "comment"
    id: Mapped[int] = mapped_column(primary_key=True)
    date: Mapped[str] = mapped_column(nullable=False)
    text: Mapped[str] = mapped_column(nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    post_id: Mapped[int] = mapped_column(ForeignKey("post.id"))

    # Hijo de:
    user: Mapped["User"] = relationship(back_populates="comments")
    post: Mapped["Post"] = relationship(back_populates="comments")

    def serialize(self):
        return {
            "id": self.id,
            "date": self.date,
            "text": self.text,
            "user_id": self.user_id,
            "post_id": self.post_id
        }

class Follows(db.Model):
    __tablename__ = "follows"
    id: Mapped[int] = mapped_column(primary_key=True)
    date: Mapped[int] = mapped_column(nullable=False)
    follower_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    followed_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

    # Hijo de:
    follower_user: Mapped["User"] = relationship(foreign_keys=[follower_id],back_populates="following")
    followed_user: Mapped["User"] = relationship(foreign_keys=[followed_id],back_populates="followers")


    # Añadir FK foreign_keys="a follower_user y followed_user"
    def serialize(self):
        return {
            "id": self.id,
            "date": self.date,
            "followed_id": self.followed_id,
            "follower_id": self.follower_id
        }
