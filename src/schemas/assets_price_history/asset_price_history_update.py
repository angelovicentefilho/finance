"""
Copyright (c) J-Tech Solucoes em Informatica.
All Rights Reserved.

This software is the confidential and proprietary information of J-Tech.
("Confidential Information"). You shall not disclose such Confidential
Information and shall use it only in accordance with the terms of the
license agreement you entered into with J-Tech.
"""
from src.schemas.assets_price_history import AssetPriceHistoryBase


class AssetPriceHistoryUpdate(AssetPriceHistoryBase):
    id: int

    class Config:
        orm_mode = True
