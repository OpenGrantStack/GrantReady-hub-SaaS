
---

# app/webhooks/ci_events.py

`python
from fastapi import APIRouter, Request, Header
from app.utils.verifysignature import verifysignature
from app.utils.logger import logger

router = APIRouter()


@router.post("/webhooks/ci-events")
async def cieventswebhook(
    request: Request,
    xhubsignature_256: str = Header(None)
):
    body = await request.body()
    verifysignature(body, xhubsignature256, "YOURWEBHOOKSECRET")

    logger.info("CI events webhook received")
    # TODO: Track CI runs, statuses, coverage events
    return {"status": "ok", "webhook": "ci-events"}
`