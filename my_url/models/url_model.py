from pydantic import BaseModel, ConfigDict


class LinkIn(BaseModel):
    # model_config = ConfigDict(from_attributes=True)
    body: str


class Link(LinkIn):
    model_config = ConfigDict(from_attributes=True)
    id: int
