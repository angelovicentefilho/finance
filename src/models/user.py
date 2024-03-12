"""
Copyright (c) J-Tech Solucoes em Informatica.
All Rights Reserved.

This software is the confidential and proprietary information of J-Tech.
("Confidential Information"). You shall not disclose such Confidential
Information and shall use it only in accordance with the terms of the
license agreement you entered into with J-Tech.
"""
from sqlalchemy.orm import relationship
from src.db.base_class import Base
from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)

    # Relações
    portfolios = relationship("Portfolio", back_populates="user")
    alerts = relationship("PriceAlert", back_populates="user")
    preferences = relationship("UserPreferences", back_populates="user", uselist=False)
    activities = relationship("ActivityLogs", back_populates="user")
