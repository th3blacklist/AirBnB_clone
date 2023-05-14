#!/usr/bin/python3
from models.base_model import BaseModel
"""class User that Inheits frtom BaseModel class """


class User(BaseModel):
    """
    args:
        email (string) - email for the user
        password (string) - password for the user
        first_name (string) - first_name of the user
        last_name (string) - Last name of the user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    
