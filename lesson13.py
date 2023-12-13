# from asyncio import run
#
# from sqlalchemy import Column, INT, VARCHAR
# from sqlalchemy.orm import DeclarativeBase
# from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
#
#
# class Base(DeclarativeBase):
#     pass
#
#
# class User(Base):
#     __tablename__ = "users"
#
#     id = Column(INT, primary_key=True)
#     username = Column(VARCHAR(32), nullable=False)
#
#
# engine = create_async_engine(url="sqlite+aiosqlite:///db.sqlite3")
# async_session_maker = async_sessionmaker(bind=engine)
#
#
# async def main():
#     async with async_session_maker() as session:  # type: AsyncSession
#         user = User(username="user 1")
#         session.add(user)
#         await session.commit()
#         await session.refresh(user)
#
#
# run(main())

# GET
# HEAD
# POST
# PUT
# PATCH
# DELETE
# from httpx import Client, AsyncClient, codes
# from http import HTTPMethod, HTTPStatus
#
# # sw_ref[0]=new&sw_ref[operation]=union&mobile_type[0]=smartphone&mobile_type[operation]=union
#
#
# async def main():
#     async with AsyncClient(base_url="https://catalog.onliner.by") as client:
#         response = await client.get(
#             url="/mobile",
#             params={
#                 "sw_ref[0]": "new",
#                 "sw_ref[operation]": "union",
#                 "mobile_type[0]": "smartphone",
#                 "mobile_type[operation]": "union"
#             }
#         )
#         print(response.status_code)
#         print(response.headers)
#
#
# if __name__ == '__main__':
#     from asyncio import run
#     run(main())
