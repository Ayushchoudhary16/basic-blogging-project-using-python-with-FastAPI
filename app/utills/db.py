from sqlalchemy.orm import declarative_base,sessionmaker
from sqlalchemy import create_engine

# db_URL="postgresql://postgres:Ayushsql@localhost:5432/"
db_URL="sqlite:///test2"

Base=declarative_base()

db_init=create_engine(db_URL)

localSession=sessionmaker(bind=db_init)

def get_db():
    db=localSession()
    try:
        yield db
    finally:
        db.close()