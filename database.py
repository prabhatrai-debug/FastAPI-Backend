#SQLAlchemy ORM-a powerful python library that lets you work with database using python classes instead of writting raw SQL queries . FastAPI doesn't force you to use any one database , but SQLAlchemy is one of the most common and flexible choices.

#             # What is ORM and WHY use it ?
#ORM lets us interact with database using python object intead of SQL -easier and less error-prone.


#✅ Advantages of ORM

# No need to write raw SQL everywhere
# Prevents SQL injection
# Cleaner code
# Easy relationships (ForeignKey)
# Easier maintenance


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

MYSQL_USER="root"
MYSQL_PASSWORD="1234"
MYSQL_HOST="localhost"
MYSQL_PORT="3306"
MYSQL_DATABASE="fastapi_db"


DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"


#connection
engine = create_engine(DATABASE_URL)

#Session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

##Base
Base=declarative_base()    


