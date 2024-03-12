"""
Copyright (c) J-Tech Solucoes em Informatica.
All Rights Reserved.

This software is the confidential and proprietary information of J-Tech.
("Confidential Information"). You shall not disclose such Confidential
Information and shall use it only in accordance with the terms of the
license agreement you entered into with J-Tech.
"""
from datetime import datetime

from pydantic import BaseModel


class AssetPriceHistoryBase(BaseModel):
    dateTime: datetime
    closingPrice: float
    openingPrice: float
    high: float
    low: float
    volume: float
