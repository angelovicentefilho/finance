"""
Copyright (c) J-Tech Solucoes em Informatica.
All Rights Reserved.

This software is the confidential and proprietary information of J-Tech.
("Confidential Information"). You shall not disclose such Confidential
Information and shall use it only in accordance with the terms of the
license agreement you entered into with J-Tech.
"""
from sqlalchemy import Column, Integer, ForeignKey, DECIMAL, DateTime
from sqlalchemy.orm import relationship
from src.db.session import Base


class AssetPriceHistory(Base):
    __tablename__ = 'asset_price_history'

    id = Column(Integer, primary_key=True, index=True)
    assetId = Column(Integer, ForeignKey('assets.id'), nullable=False)
    dateTime = Column(DateTime, index=True, nullable=False)
    closingPrice = Column(DECIMAL(18, 4), nullable=False)
    openingPrice = Column(DECIMAL(18, 4), nullable=False)
    high = Column(DECIMAL(18, 4), nullable=False)
    low = Column(DECIMAL(18, 4), nullable=False)
    volume = Column(DECIMAL(18, 4), nullable=False)

    # Relações
    asset = relationship("Asset", back_populates="price_history")
