"""
Copyright (c) J-Tech Solucoes em Informatica.
All Rights Reserved.

This software is the confidential and proprietary information of J-Tech.
("Confidential Information"). You shall not disclose such Confidential
Information and shall use it only in accordance with the terms of the
license agreement you entered into with J-Tech.
"""

from src.db.base_class import Base

from sqlalchemy import Column, Integer, ForeignKey, DECIMAL, Enum, DateTime
from sqlalchemy.orm import relationship


class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True, index=True)
    portfolioId = Column(Integer, ForeignKey('portfolios.id'), nullable=False)
    assetId = Column(Integer, ForeignKey('assets.id'), nullable=False)
    type = Column(Enum('buy', 'sell'), nullable=False)
    quantity = Column(DECIMAL(18, 4), nullable=False)
    price = Column(DECIMAL(18, 4), nullable=False)
    transactionDate = Column(DateTime, nullable=False)

    # Relações
    portfolio = relationship("Portfolio", back_populates="transactions")
    asset = relationship("Asset", back_populates="transactions")
