from pydantic import BaseModel, Field
from typing import Annotated, Literal
import datetime

class CookieConfig(BaseModel):
    key: Annotated[str | None, Field()]= None
    value: Annotated[str | None, Field()] = None
    expires: Annotated[datetime.datetime | None, Field()] = None
    path: Annotated[str, Field()] = '/'
    samesite: Annotated[Literal['none', 'lax', 'strict'], Field()] = 'lax'
    secure: Annotated[bool, Field()]=True
    httponly: Annotated[bool, Field()]=True
