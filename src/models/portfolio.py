"""
Copyright (c) J-Tech Solucoes em Informatica.
All Rights Reserved.

This software is the confidential and proprietary information of J-Tech.
("Confidential Information"). You shall not disclose such Confidential
Information and shall use it only in accordance with the terms of the
license agreement you entered into with J-Tech.
"""

from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from src.db.base_class import Base


class Portfolio(Base):
    __tablename__ = "portfolios"

    id = Column(Integer, primary_key=True, index=True)
    userId = Column(Integer, ForeignKey('users.id'), nullable=False)
    name = Column(String, index=True, nullable=False)
    description = Column(Text, nullable=True)

    # Relações
    user = relationship("User", back_populates="portfolios")
    assets = relationship("PortfolioAssetDetails", back_populates="portfolio")
    transactions = relationship("Transaction", back_populates="portfolio")
