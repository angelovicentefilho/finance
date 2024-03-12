"""
Copyright (c) J-Tech Solucoes em Informatica.
All Rights Reserved.

This software is the confidential and proprietary information of J-Tech.
("Confidential Information"). You shall not disclose such Confidential
Information and shall use it only in accordance with the terms of the
license agreement you entered into with J-Tech.
"""

from sqlalchemy import Column, ForeignKey, Integer, DECIMAL
from sqlalchemy.orm import relationship
from src.db.session import Base


class PortfolioAssetDetails(Base):
    __tablename__ = 'portfolio_asset_details'

    portfolioId = Column(Integer, ForeignKey('portfolios.id'), primary_key=True)
    assetId = Column(Integer, ForeignKey('assets.id'), primary_key=True)
    quantity = Column(DECIMAL(18, 4), nullable=False)
    averageAcquisitionValue = Column(DECIMAL(18, 4), nullable=False)
    currentValue = Column(DECIMAL(18, 4), nullable=False)
    profitability = Column(DECIMAL(18, 4), nullable=False)

    # Relações
    portfolio = relationship("Portfolio", back_populates="assets")
    asset = relationship("Asset", back_populates="portfolio_asset_details")
