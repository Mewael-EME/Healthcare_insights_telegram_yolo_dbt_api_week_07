# api/schemas.py
from pydantic import BaseModel

class TopProduct(BaseModel):
    product: str
    count: int

class ChannelActivity(BaseModel):
    date: str
    message_count: int

class MessageSearch(BaseModel):
    message: str
    channel: str
    sent_at: str

