
---

# app/webhooks/notifications.py

`python
from fastapi import APIRouter, Request, Header
from app.utils.verifysignature import verifysignature
from app.utils.logger import logger

router = APIRouter()


@router.post("/webhooks/notifications")
async def notifications_webhook(
    request: Request,
    xhubsignature_256: str = Header(None)
):
    body = await request.body()
    verifysignature(body, xhubsignature256, "YOURWEBHOOKSECRET")

    logger.info("Notifications webhook received")
    # TODO: Forward important events to Slack/Teams/email
    return {"status": "ok", "webhook": "notifications"}
`