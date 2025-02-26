from oreoweb import Request, Response, Router

from .models import Link

router = Oreoweb()


@router.route("/urls", methods=["post"])
async def shorten_url(req: Request, res: Response):
    link, _ = await Link.objects.get_or_create(**await req.json())
    res.json = dict(link)
    res.status_code = 201


@router.route("/urls/{hash}")
async def retrieve_url(req: Request, res: Response, hash: str):
    link = await Link.objects.get(hash=hash)
    res.json = dict(link)
