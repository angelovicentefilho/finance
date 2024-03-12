"""
Copyright (c) J-Tech Solucoes em Informatica.
All Rights Reserved.

This software is the confidential and proprietary information of J-Tech.
("Confidential Information"). You shall not disclose such Confidential
Information and shall use it only in accordance with the terms of the
license agreement you entered into with J-Tech.
"""
from pydantic import BaseModel


class AssetBase(BaseModel):
    name: str
    type: str
    ticker: str

    class Config:
        orm_mode = True
