
---

# app/webhooks/local_tunnel.py

`python
from fastapi import APIRouter, Request, Header
from app.utils.verifysignature import verifysignature
from app.utils.logger import logger

router = APIRouter()


@router.post("/webhooks/local-tunnel")
async def localtunnelwebhook(
    request: Request,
    xhubsignature_256: str = Header(None)
):
    body = await request.body()
    verifysignature(body, xhubsignature256, "YOURWEBHOOKSECRET")

    logger.info("Local tunnel webhook received (ngrok/Cloudflare)")
    # TODO: Used only for local development tunnels
    return {"status": "ok", "webhook": "local-tunnel"}
`