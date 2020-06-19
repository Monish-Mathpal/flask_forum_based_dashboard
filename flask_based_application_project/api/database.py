from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

path = "/home/monish/flask_forum_based_dashboard/flask_based_application_project/forum_based_analytic_dboard_app/site.db"
SQLALCHEMY_DATABASE_URL = "sqlite:////"+path

# SQLALCHEMY_DATABASE_URL = "sqlite:///site.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()