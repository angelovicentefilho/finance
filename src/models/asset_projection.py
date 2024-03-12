"""
Copyright (c) J-Tech Solucoes em Informatica.
All Rights Reserved.

This software is the confidential and proprietary information of J-Tech.
("Confidential Information"). You shall not disclose such Confidential
Information and shall use it only in accordance with the terms of the
license agreement you entered into with J-Tech.
"""
from sqlalchemy import Column, Integer, ForeignKey, DateTime, DECIMAL, String
from sqlalchemy.orm import relationship
from src.db.base_class import Base


class AssetProjection(Base):
    __tablename__ = 'asset_projections'

    id = Column(Integer, primary_key=True, index=True)
    assetId = Column(Integer, ForeignKey('assets.id'), nullable=False)
    projectionDate = Column(DateTime, index=True, nullable=False)
    projectedPrice = Column(DECIMAL(18, 4), nullable=False)
    projectionMethod = Column(String, nullable=False)

    asset = relationship("Asset", back_populates="projections")
