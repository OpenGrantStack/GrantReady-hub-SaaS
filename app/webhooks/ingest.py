
---

# app/webhooks/ingest.py

`python
from fastapi import APIRouter, Request, Header
from app.utils.verifysignature import verifysignature
from app.utils.logger import logger

router = APIRouter()


@router.post("/webhooks/ingest")
async def ingest_webhook(
    request: Request,
    xhubsignature_256: str = Header(None)
):
    body = await request.body()
    verifysignature(body, xhubsignature256, "YOURWEBHOOKSECRET")

    logger.info("Ingest webhook received")
    # TODO: Push to raw storage / queue
    return {"status": "ok", "webhook": "ingest"}
`