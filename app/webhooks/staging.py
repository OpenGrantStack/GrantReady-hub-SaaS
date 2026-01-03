
---

# app/webhooks/staging.py

`python
from fastapi import APIRouter, Request, Header
from app.utils.verifysignature import verifysignature
from app.utils.logger import logger

router = APIRouter()


@router.post("/webhooks/staging")
async def staging_webhook(
    request: Request,
    xhubsignature_256: str = Header(None)
):
    body = await request.body()
    verifysignature(body, xhubsignature256, "YOURWEBHOOKSECRET")

    logger.info("Staging webhook received")
    # TODO: Use for staging/pre-production testing
    return {"status": "ok", "webhook": "staging"}
`