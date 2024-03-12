"""
Copyright (c) J-Tech Solucoes em Informatica.
All Rights Reserved.

This software is the confidential and proprietary information of J-Tech.
("Confidential Information"). You shall not disclose such Confidential
Information and shall use it only in accordance with the terms of the
license agreement you entered into with J-Tech.
"""

from src.models.user import User


def test_create_user(session):
    test_user = User(name="username", email="test@email.com", password="password")
    session.add(test_user)
    session.commit()

    user_from_database = session.query(User).filter_by(email="test@email.com").first()

    assert user_from_database is not None
    assert user_from_database.name == "username"
    assert user_from_database.email == "test@email.com"
    assert user_from_database.password != "password1"
