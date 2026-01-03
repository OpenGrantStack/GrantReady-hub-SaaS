
---

# app/webhooks/ledger.py

`python
from fastapi import APIRouter, Request, Header
from app.utils.verifysignature import verifysignature
from app.utils.logger import logger

router = APIRouter()


@router.post("/webhooks/ledger")
async def ledger_webhook(
    request: Request,
    xhubsignature_256: str = Header(None)
):
    body = await request.body()
    verifysignature(body, xhubsignature256, "YOURWEBHOOKSECRET")

    logger.info("Ledger webhook received")
    # TODO: Persist normalized events to financial/effort ledger
    return {"status": "ok", "webhook": "ledger"}
`