"""
Copyright (c) J-Tech Solucoes em Informatica.
All Rights Reserved.

This software is the confidential and proprietary information of J-Tech.
("Confidential Information"). You shall not disclose such Confidential
Information and shall use it only in accordance with the terms of the
license agreement you entered into with J-Tech.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from src.db.base_class import Base


class Asset(Base):
    __tablename__ = 'assets'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    type = Column(String, index=True)  # Por exemplo, 'stock', 'crypto'
    ticker = Column(String, index=True, unique=True)  # Identificador único do ativo

    # Relações
    price_history = relationship("AssetPriceHistory", back_populates="asset")
    portfolio_asset_details = relationship("PortfolioAssetDetails", back_populates="asset")
    transactions = relationship("Transaction", back_populates="asset")
    projections = relationship("AssetProjection", back_populates="asset")
    alerts = relationship("PriceAlert", back_populates="asset")
