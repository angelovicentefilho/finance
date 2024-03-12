"""
Copyright (c) J-Tech Solucoes em Informatica.
All Rights Reserved.

This software is the confidential and proprietary information of J-Tech.
("Confidential Information"). You shall not disclose such Confidential
Information and shall use it only in accordance with the terms of the
license agreement you entered into with J-Tech.
"""

from sqlalchemy import Column, Integer, ForeignKey, DECIMAL, Enum, Boolean
from sqlalchemy.orm import relationship
from src.db.session import Base


class PriceAlert(Base):
    __tablename__ = 'price_alerts'

    id = Column(Integer, primary_key=True, index=True)
    userId = Column(Integer, ForeignKey('users.id'), nullable=False)
    assetId = Column(Integer, ForeignKey('assets.id'), nullable=False)
    triggerPrice = Column(DECIMAL(18, 4), nullable=False)
    alertType = Column(Enum('above', 'below'), nullable=False)
    isActive = Column(Boolean, default=True, nullable=False)

    # Relações
    user = relationship("User", back_populates="alerts")
    asset = relationship("Asset", back_populates="alerts")
