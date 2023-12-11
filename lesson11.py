# from sqlite3 import connect
#
#
# conn = connect("db.sqlite3")
# cur = conn.cursor()
#
#
# cur.execute("""
#     CREATE TABLE IF NOT EXISTS users (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         username VARCHAR ( 24 ) NOT NULL,
#         email VARCHAR ( 128 ) NOT NULL UNIQUE,
#         is_active BOOLEAN DEFAULT ( false ),
#         points SMALLINT NOT NULL DEFAULT ( 0 ) CHECK ( points >= 0 )
#     );
# """)
# conn.commit()
#
# cur.execute("""
#     CREATE TABLE IF NOT EXISTS posts (
#         id INTEGER PRIMARY KEY AUTOINCREMENT ,
#         title VARCHAR ( 128 ) NOT NULL ,
#         body TEXT NOT NULL ,
#         date_created TIMESTAMP NOT NULL ,
#         user_id INTEGER NOT NULL,
#         FOREIGN KEY ( user_id ) REFERENCES users ( id )
#         ON DELETE RESTRICT ON UPDATE CASCADE
#     );
# """)
# conn.commit()
#
# cur.execute("""
#     CREATE TABLE IF NOT EXISTS products (
#         article VARCHAR(128) PRIMARY KEY ,
#         name VARCHAR(256) NOT NULL ,
#         price DECIMAL (8, 2) NOT NULL CHECK ( price > 0 )
#     );
# """)
#
# cur.execute("""
#     CREATE TABLE IF NOT EXISTS orders (
#         id INTEGER PRIMARY KEY AUTOINCREMENT ,
#         user_id INTEGER NOT NULL ,
#         FOREIGN KEY ( user_id ) REFERENCES users ( id )
#         ON DELETE RESTRICT ON UPDATE CASCADE
#     );
# """)
#
# cur.execute("""
#     CREATE TABLE IF NOT EXISTS order_items (
#         order_id INTEGER NOT NULL ,
#         product_article VARCHAR (128) NOT NULL ,
#         count SMALLINT NOT NULL CHECK ( count > 0 ) DEFAULT (1),
#         PRIMARY KEY (order_id, product_article),
#         FOREIGN KEY (order_id) REFERENCES orders (id)
#         ON DELETE RESTRICT ON UPDATE CASCADE,
#         FOREIGN KEY (product_article) REFERENCES products (article)
#         ON DELETE RESTRICT ON UPDATE CASCADE
#     );
# """)

# cur.execute("CREATE INDEX user_id_index ON posts (user_id);")

# cur.execute(
#     # "INSERT INTO users (username, email) VALUES (:username, :email);",
#     # {"username": "vasya", "email": "vasya@gmail.com"}
#
#     "INSERT INTO users (username, email) VALUES (?, ?);",
#     ("vasya", "vasya@gmail.com")
# )
# conn.commit()

# cur.execute("""
#     SELECT email, username, points FROM users WHERE points >= (SELECT AVG(points) FROM users);
# """)
# print(cur.fetchall())


# cur.execute("""
#     SELECT * FROM users ORDER BY is_active DESC , points ;
# """)
# print(cur.fetchall())

# cur.execute("""
#     SELECT users.email, posts.title FROM users LEFT JOIN posts ON users.id = posts.user_id;
# """)
# print(cur.fetchall())

# cur.execute("""
#     UPDATE users SET email = ?, username = ? WHERE id = ?;
# """, ("petya@gmail.com", "petya", 1))
# conn.commit()

# cur.execute("DELETE FROM users;")
# conn.commit()


# from psycopg2.extras import NamedTupleConnection
#
#
# with NamedTupleConnection("postgresql://admin:admin@0.0.0.0:5432/admin") as conn:
#     with conn.cursor() as cur:
#         cur.execute("select avg(id) as avg_id from categories;")
#         print(cur.fetchall())
from datetime import datetime, UTC
from typing import Type

from sqlalchemy import (
    Column,
    INT,
    VARCHAR,
    BOOLEAN,
    ForeignKey,
    CheckConstraint,
    TEXT,
    TIMESTAMP,
    create_engine,
    update,
    delete,
    select,
    or_,
    and_,
    any_,
    all_
)
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import DeclarativeBase, relationship, sessionmaker, synonym, Session, selectinload
from sqlalchemy.sql.functions import count, func

# sqlalchemy < 2.0
# Base = declarative_base()


engine = create_engine(url="postgresql://bh72:VeryStrongPass@0.0.0.0:5432/bh72")
session_maker = sessionmaker(bind=engine)


# sqlalchemy >= 2.0
class Base(DeclarativeBase):

    def update_from_attributes(self, obj: "BaseModel"):
        for k, v in obj.model_dump(exclude_none=True, exclude_defaults=True, exclude_unset=True).items():
            if hasattr(self, k):
                setattr(self, k, v)


class User(Base):
    __tablename__ = "users"
    __table_args__ = (
        CheckConstraint("char_length(username) >= 2 and username not like '% %'"),
        CheckConstraint("email not like '% %'")
    )

    id = Column(INT, primary_key=True)
    email = Column(VARCHAR(128), nullable=False, unique=True)
    username = Column(VARCHAR(32), nullable=False)
    is_active = Column(BOOLEAN, default=False)

    posts = relationship(argument="Post", back_populates="user")
    pk = synonym(name="id")

    def __str__(self):
        return self.email

    def __repr__(self):
        return self.email


class Post(Base):
    __tablename__ = "posts"

    id = Column(INT, primary_key=True)
    title = Column(VARCHAR(128), nullable=False)
    body = Column(TEXT, nullable=False)
    date_created = Column(TIMESTAMP(timezone=True), default=lambda: datetime.now(tz=UTC), nullable=False)
    is_published = Column(BOOLEAN, server_default="false")
    user_id = Column(
        INT,
        ForeignKey(column="users.id", onupdate="CASCADE", ondelete="RESTRICT"),
        nullable=False
    )

    user = relationship(argument="User", back_populates="posts")


# Base.metadata.create_all(bind=engine)
# with session_maker() as session:
#     user1 = User(
#         email="vasy@gmail.com",
#         username="vasya"
#     )
#     user2 = User(
#         email="petya@gmail.com",
#         username="petya"
#     )
#     session.add_all((user1, user2))
#     try:
#         session.commit()
#     except IntegrityError:
#         pass
#     # else:
#         # session.refresh(user1)
#         # session.refresh(user2)
#     print(user1.id)
#     print(user2.id)


# with session_maker() as session:  # type: Session
#     user = session.get(User, 1)
#     post = Post(
#         title="Post 1",
#         body="description",
#         user=user
#     )
#     session.add(post)
#     session.commit()


# with session_maker() as session:  # type: Session
#     obj = session.query(Post.id + 5)
#     print(obj)
    # obj = session.get(entity=User, ident=3)
    # objs = session.query(User).filter(User.id.in_((1, 2, 3))).order_by(User.email.desc()).all()
    # print(objs)
    # objs = session.scalars(
    #     select(User)
    #     .filter(User.id.in_((1, 2, 3)))
    #     .order_by()
    # ).all()
    # print(objs)
    # c = session.scalar(
    #     select(count(User.id))
    # )
    # print(c)
    # session.scalars(
    #     select(User)
    #     .filter(or_(User.id >= 1, User.id == 2))
    # )

    # objs = session.execute(
    #     select(User, Post)
    #     .join(target=Post, onclause=User.id == Post.user_id, isouter=True)
    # ).all()
    # print(objs)
    # obj = session.get(User, 1)
    # obj.email = "vasya@yahoo.com"
    # post = Post(
    #     title="Post 2",
    #     body="Description"
    # )
    # obj.posts.append(post)
    # session.commit()

    # obj = session.get(User, 1, options=[selectinload(User.posts)])
    # print(obj.posts)
    # users = session.query(User).options(selectinload(User.posts)).all()
    # print(users)

    # session.execute(
    #     update(User)
    #     .filter(User.id.in_((1, 2,)))
    #     .values(is_active=True)
    # )
    # session.commit()

    # obj = session.get(User, 2)
    # session.delete(obj)
    # session.commit()

    # session.execute(
    #     delete(Post)
        # .filter(Post.user.email == "vasya@yahoo.com")
    # )
    # session.commit()

    # obj = session.scalar(
    #     select(Post)
    #     .filter(or_(func.upper(Post.title).contains("POST"), func.upper(Post.body).contains("POST")))
    # )
    # print(obj)

from pydantic import BaseModel


class UserDetail(BaseModel):
    id: int = None
    email: str
    username: str
    is_active: bool = False
    # posts: list["PostDetail"] = []


class PostDetail(BaseModel):
    id: int
    title: str
    body: str
    date_created: datetime
    is_published: bool
    user_id: int


# with session_maker() as session:
#     user = UserDetail(
#         id=1,
#         email="vasek@gmail.com",
#         username="vasek"
#     )
#     obj = session.get(User, 1)
#     obj.update_from_attributes(obj=user)
#     session.commit()
    # obj = session.get(User, 1, options=[selectinload(User.posts)])
    # user = UserDetail.model_validate(obj=obj, from_attributes=True)
    # print(user)
    # user = UserDetail(
    #     email="petya@gmail.com",
    #     username="petya"
    # )
    # obj = User(**user.model_dump())
    # session.add(obj)
    # session.commit()


from abc import ABC, abstractmethod


class AbstractRepository(ABC):

    schema: Type[BaseModel]

    @abstractmethod
    def get(self, pk) -> BaseModel | None:
        pass

    @abstractmethod
    def create(self, obj: BaseModel) -> BaseModel:
        pass

    @abstractmethod
    def update(self, obj: BaseModel) -> BaseModel:
        pass

    @abstractmethod
    def delete(self, pk) -> None:
        pass


class SQLAlchemyRepository(AbstractRepository):
    model: Type[Base]

    def __init__(self, session_maker) -> None:  # noqa
        self.session_maker = session_maker

    def get(self, pk) -> BaseModel:
        with self.session_maker() as session:
            obj = session.get(self.model, pk)
            if obj is not None:
                return self.schema.model_validate(obj=obj, from_attributes=True)

    def create(self, obj: BaseModel) -> BaseModel:
        with self.session_maker() as session:
            orm_obj = self.model(**obj.model_dump())
            session.add(orm_obj)
            session.commit()
            return self.schema.model_validate(obj=orm_obj, from_attributes=True)

    def update(self, obj: BaseModel) -> BaseModel:
        with self.session_maker() as session:
            session.execute(
                update(self.model)
                .values(**obj.model_dump(exclude={"id"}))
                .filter(self.model.id == obj.id)
            )
            session.commit()
            return obj

    def delete(self, pk) -> None:
        with self.session_maker() as session:
            session.execute(
                delete(self.model)
                .filter(self.model.id == pk)
            )
            session.commit()


class SQLRepository(AbstractRepository):

    def get(self, pk) -> BaseModel | None:
        pass

    def create(self, obj: BaseModel) -> BaseModel:
        pass

    def update(self, obj: BaseModel) -> BaseModel:
        pass

    def delete(self, pk) -> None:
        pass


class UserRepository(SQLAlchemyRepository):
    model = User
    schema = UserDetail


class PostRepository(SQLAlchemyRepository):
    model = Post
    schema = PostDetail


# user_repository = UserRepository(session_maker=session_maker)
# print(user_repository.get(pk=1))
