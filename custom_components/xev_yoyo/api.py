import logging
import asyncio
import async_timeout
import hashlib
import json

_LOGGER = logging.getLogger(__name__)

class XevApi:
    def __init__(self, session, mobile, password, region_code, device_uuid):
        self._session = session
        self._mobile = str(mobile).strip()
        self._password = str(password).strip()
        self._region_code = str(region_code).strip()
        self._uuid = device_uuid.upper()
        self._device_token = hashlib.sha256(self._uuid.lower().encode()).hexdigest()
        
        self._base_headers = {
            "Accept": "application/json",
            "Accept-Language": "it",
            "appKey": "3be9c04837654cc09e97dabf63c9fe77",
            "clientOs": "1",
            "Connection": "keep-alive",
            "Content-Type": "application/json",
            "deviceToken": self._device_token,
            "Host": "app.xevapp.com",
            "User-Agent": "YOYO/2.3.0 (iPhone; iOS 26.2.1; Scale/3.00)",
            "uuid": self._uuid,
            "version": "2.3.0"
        }

    async def _request(self, method, url, headers, json_data=None):
        data = json.dumps(json_data, separators=(',', ':')) if json_data else None
        try:
            async with async_timeout.timeout(10):
                async with self._session.request(method, url, headers=headers, data=data) as res:
                    return await res.json()
        except Exception as e:
            _LOGGER.error(f"Errore XEV durante la chiamata {url}: {e}")
            return None

    async def login(self):
        await self._request("POST", "https://app.xevapp.com/gw/portal/verifyPhone", 
                          self._base_headers, {"mobilePhone": self._mobile, "regionCode": self._region_code})
        
        payload = {
            "mobilePhone": self._mobile,
            "regionCode": self._region_code,
            "password": hashlib.md5(self._password.encode()).hexdigest()
        }
        data = await self._request("POST", "https://app.xevapp.com/gw/portal/passwordLogin", self._base_headers, payload)
        
        if data and data.get("code") == "000000":
            token = data["data"]["accessToken"]
            auth_h = {**self._base_headers, "Authorization": f"Bearer {token}"}
            
            await self._request("GET", "https://app.xevapp.com/gw/pay/publishKey", auth_h)
            await self._request("GET", "https://app.xevapp.com/gw/pay/getPaymentBind", auth_h)
            
            await asyncio.sleep(1)
            return token, None
        
        return None, data.get("message", "Login fallito")

    async def get_vehicles(self, token):
        headers = {**self._base_headers, "Authorization": f"Bearer {token}"}
        data = await self._request("GET", "https://app.xevapp.com/gw/vehicle/getVehicleList", headers)
        
        if data and data.get("code") == "000000":
            return data.get("data", [])
        return []
    
    async def get_vehicle_status(self, token, vehicle_id):
        url = "https://app.xevapp.com/gw/vehicleControl/acquireVehicleInfo"
        headers = {
            **self._base_headers,
            "Authorization": f"Bearer {token}"
        }
        payload = {
            "vehicleId": vehicle_id,
            "vehicleAction": "bv_state00001"
        }
        
        data = await self._request("POST", url, headers, payload)
        if data and data.get("code") == "000000":
            return data.get("data", {})
        return {}