
---

# app/webhooks/events_router.py

`python
from fastapi import APIRouter, Request, Header
from app.utils.verifysignature import verifysignature
from app.utils.logger import logger

router = APIRouter()


@router.post("/webhooks/events-router")
async def eventsrouterwebhook(
    request: Request,
    xhubsignature_256: str = Header(None)
):
    body = await request.body()
    verifysignature(body, xhubsignature256, "YOURWEBHOOKSECRET")

    logger.info("Events router webhook received")
    # TODO: Inspect event type and route internally
    return {"status": "ok", "webhook": "events-router"}
`