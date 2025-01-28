from fastapi import APIRouter
from models.url_model import Link, LinkIn

router = APIRouter()


@router.post("/shortner", response_model=Link)
def make_shorturl(link: LinkIn):
    return {"body": link.body, "id": 2}
