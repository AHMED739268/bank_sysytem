

from sqlalchemy import create_engine, Column, Integer, String, Text, Float
from sqlalchemy.orm import declarative_base, sessionmaker


DATABASE_URL = "postgresql+psycopg2://aabdallah:1682001@localhost:5432/users"


engine = create_engine(DATABASE_URL)
Base = declarative_base()


class User(Base):

    __tablename__ = "usersinfoo"

    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    email = Column(String(50), nullable=False)
    password = Column(Text, nullable=False)
    balance = Column(Float, default=0.0)  # Added balance column for bank functionality

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}', email='{self.email}', balance={self.balance})>"


# Create tables if they don't exist
Base.metadata.create_all(engine)

# Session factory
Session = sessionmaker(bind=engine)


def get_session():
    """Get a new database session"""
    return Session()