from fastapi import FastAPI, Header, HTTPException
from typing import Optional, List

app = FastAPI()

# 1. Basic user-agent header
@app.get("/header-example/")
async def read_header(user_agent: Optional[str] = Header(default=None)):
    return {"User-Agent": user_agent}

# 2. Required custom header
@app.get("/custom-header/")
async def get_custom_header(x_token: str = Header(...)):
    return {"X-Token": x_token}

# 3. Optional custom header with a default value
@app.get("/optional-header/")
async def get_optional_header(x_lang: str = Header(default="en")):
    return {"X-Lang": x_lang}

# 4. Multiple values in header (like: `X-Tags: tag1, tag2`)
@app.get("/multi-header/")
async def get_multi_header(x_tags: List[str] = Header(default=[])):
    return {"X-Tags": x_tags}

# 5. Combining required and optional headers
@app.get("/mixed-headers/")
async def mixed_headers(
    x_token: str = Header(...),
    x_lang: Optional[str] = Header(default="en")
):
    return {
        "X-Token": x_token,
        "X-Lang": x_lang
    }

# 6. Header-based authorization logic
@app.get("/secure-data/")
async def secure_data(x_token: str = Header(...)):
    if x_token != "secure123":
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"data": "Secret information"}

# 7. Inspecting common headers
@app.get("/inspect/")
async def inspect_headers(
    user_agent: Optional[str] = Header(default=None),
    accept_language: Optional[str] = Header(default=None),
):
    return {
        "User-Agent": user_agent,
        "Accept-Language": accept_language,
    }

# 8. Optional boolean from header
@app.get("/feature-flag/")
async def feature_flag(x_debug: Optional[bool] = Header(default=False)):
    return {
        "debug_mode": x_debug
    }

# 9. Header to simulate versioning
@app.get("/version/")
async def versioning(x_api_version: Optional[str] = Header(default="v1")):
    return {"API-Version": x_api_version}
