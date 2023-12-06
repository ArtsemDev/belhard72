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

from sqlalchemy import Column, INT, VARCHAR, BOOLEAN, ForeignKey, CheckConstraint, TEXT, TIMESTAMP, create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import DeclarativeBase, relationship, sessionmaker


# sqlalchemy < 2.0
# Base = declarative_base()


engine = create_engine(url="postgresql://bh72:VeryStrongPass@0.0.0.0:5432/bh72")
session_maker = sessionmaker(bind=engine)


# sqlalchemy >= 2.0
class Base(DeclarativeBase):
    pass


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
with session_maker() as session:
    user1 = User(
        email="vasy@gmail.com",
        username="vasya"
    )
    user2 = User(
        email="petya@gmail.com",
        username="petya"
    )
    session.add_all((user1, user2))
    try:
        session.commit()
    except IntegrityError:
        pass
    # else:
        # session.refresh(user1)
        # session.refresh(user2)
    print(user1.id)
    print(user2.id)

