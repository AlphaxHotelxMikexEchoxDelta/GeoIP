from shodan import Shodan
from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/ip/{ip}")
async def get_ip(ip: str, key: Optional[str] = None):
    if key is None:
        return {"Error": "Please provide a valid API key"}
    else:
        try:
            api = Shodan(key)
            res = api.host(ip)
            return {
                "longitude": res["longitude"],
                "latitude": res["latitude"]
            }
        except Exception as e:
            return {"Error": str(e)}
