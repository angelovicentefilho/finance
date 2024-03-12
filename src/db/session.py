"""
Copyright (c) J-Tech Solucoes em Informatica.
All Rights Reserved.

This software is the confidential and proprietary information of J-Tech.
("Confidential Information"). You shall not disclose such Confidential
Information and shall use it only in accordance with the terms of the
license agreement you entered into with J-Tech.
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

DATABASE_URL = "sqlite:///./finance.db"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
