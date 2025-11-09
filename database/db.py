import string
from sqlalchemy import Integer, create_engine, Column, BigInteger, String, true
from sqlalchemy.orm import Session, base, declarative_base, sessionmaker

database_url = "postgresql://postgres:solohiddin@localhost:5432/bot2_audio"
# database_url = "postgresql://postgres:[YOUR-PASSWORD]@db.gwxdozrfildddbfvnsqt.supabase.co:5432/postgres"
engine = create_engine(database_url)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()








# from sqlalchemy import create_engine
# # from sqlalchemy.pool import NullPool
# from dotenv import load_dotenv
# import os

# # Load environment variables from .env
# load_dotenv()

# # Fetch variables
# USER = os.getenv("user")
# PASSWORD = os.getenv("password")
# HOST = os.getenv("host")
# # PORT = os.getenv("port")
# DBNAME = os.getenv("dbname")
# print("here")
# # Construct the SQLAlchemy connection string
# DATABASE_URL = f"postgresql://{USER}:{PASSWORD}@{HOST}:6543/{DBNAME}?sslmode=require"
# # DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:5432/{DBNAME}?sslmode=require"
# # DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}?sslmode=require"
# print("try to connect")

# # Create the SQLAlchemy engine
# engine = create_engine(DATABASE_URL)
# # If using Transaction Pooler or Session Pooler, we want to ensure we disable SQLAlchemy client side pooling -
# # https://docs.sqlalchemy.org/en/20/core/pooling.html#switching-pool-implementations
# # engine = create_engine(DATABASE_URL, poolclass=NullPool)


# # Test the connection
# try:
#     print("im in")

#     with engine.connect() as connection:
#         print("Connection successful!")
# except Exception as e:
#     print(f"Failed to connect: {e}")

# print("and here")
# # DATABASE_URL = f"postgresql+psycopg2://postgres:Soloh1dd1n$!@db.gwxdozrfildddbfvnsqt.supabase.co:5432/postgres?sslmode=require"