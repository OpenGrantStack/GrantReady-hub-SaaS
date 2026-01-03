
---

# app/webhooks/dev.py

`python
from fastapi import APIRouter, Request, Header
from app.utils.verifysignature import verifysignature
from app.utils.logger import logger

router = APIRouter()


@router.post("/webhooks/dev")
async def dev_webhook(
    request: Request,
    xhubsignature_256: str = Header(None)
):
    body = await request.body()
    verifysignature(body, xhubsignature256, "YOURWEBHOOKSECRET")

    logger.info("Dev webhook received")
    # TODO: Use for development/testing only
    return {"status": "ok", "webhook": "dev"}
`