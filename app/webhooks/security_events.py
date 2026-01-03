
---

# app/webhooks/security_events.py

`python
from fastapi import APIRouter, Request, Header
from app.utils.verifysignature import verifysignature
from app.utils.logger import logger

router = APIRouter()


@router.post("/webhooks/security-events")
async def securityeventswebhook(
    request: Request,
    xhubsignature_256: str = Header(None)
):
    body = await request.body()
    verifysignature(body, xhubsignature256, "YOURWEBHOOKSECRET")

    logger.warning("Security event webhook received")
    # TODO: Send to security pipeline / alerting
    return {"status": "ok", "webhook": "security-events"}
`