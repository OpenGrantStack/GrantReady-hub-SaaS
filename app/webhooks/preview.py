
---

# app/webhooks/preview.py

`python
from fastapi import APIRouter, Request, Header
from app.utils.verifysignature import verifysignature
from app.utils.logger import logger

router = APIRouter()


@router.post("/webhooks/preview")
async def preview_webhook(
    request: Request,
    xhubsignature_256: str = Header(None)
):
    body = await request.body()
    verifysignature(body, xhubsignature256, "YOURWEBHOOKSECRET")

    logger.info("Preview webhook received")
    # TODO: Trigger preview builds / ephemeral envs
    return {"status": "ok", "webhook": "preview"}
`