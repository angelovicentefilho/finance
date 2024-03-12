"""
Copyright (c) J-Tech Solucoes em Informatica.
All Rights Reserved.

This software is the confidential and proprietary information of J-Tech.
("Confidential Information"). You shall not disclose such Confidential
Information and shall use it only in accordance with the terms of the
license agreement you entered into with J-Tech.
"""

from sqlalchemy import Column, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship
from src.db.session import Base


class UserPreferences(Base):
    __tablename__ = 'user_preferences'

    id = Column(Integer, primary_key=True, index=True)
    userId = Column(Integer, ForeignKey('users.id'), nullable=False, unique=True)
    visualizationSettings = Column(Text, nullable=True)
    notificationSettings = Column(Text, nullable=True)

    # Relações
    user = relationship("User", back_populates="preferences")
