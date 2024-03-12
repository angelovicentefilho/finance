"""
Copyright (c) J-Tech Solucoes em Informatica.
All Rights Reserved.

This software is the confidential and proprietary information of J-Tech.
("Confidential Information"). You shall not disclose such Confidential
Information and shall use it only in accordance with the terms of the
license agreement you entered into with J-Tech.
"""

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.db.base_class import Base

DATABASE_URI = "sqlite:///./test.db"
engine = create_engine(DATABASE_URI, echo=True)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="function")
def session():
    """
    This fixture creates a new database session for a test to use. It also creates the schema for the database and
    drops it after the test is done.
    :return: A database session
    """
    Base.metadata.create_all(bind=engine)  # Create the schema
    connection = engine.connect()  # Connect to the database
    transaction = connection.begin()  # Begin a non-ORM transaction
    db_session = TestingSessionLocal(bind=connection)  # Bind an individual Session to the connection

    yield db_session  # Use the session in the test

    db_session.close()  # Rollback the non-ORM transaction
    transaction.rollback()  # Close the connection
    connection.close()  # Return the connection to the Engine
    Base.metadata.drop_all(bind=engine)  # Drop the schema
