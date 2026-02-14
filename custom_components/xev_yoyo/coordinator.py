import logging
from datetime import timedelta
import aiohttp
import async_timeout

from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from .const import DOMAIN, API_URL

_LOGGER = logging.getLogger(__name__)

class XevYoyoCoordinator(DataUpdateCoordinator):

    def __init__(self, hass, entry_data):
        self.entry_data = entry_data
        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=timedelta(seconds=300),
        )

    async def _async_update_data(self):
        """Recupero dati da API"""
        headers = {
            "User-Agent": "YOYO/2.1.3 (iPhone; iOS 26.1; Scale/3.00)",
            "Accept": "application/json",
            "Content-Type": "application/json",
            "uuid": self.entry_data["uuid"],
            "appKey": self.entry_data["app_key"],
            "Authorization": f"Bearer {self.entry_data['token']}",
        }
        
        payload = {
            "vehicleId": self.entry_data["vehicle_id"],
            "vehicleAction": "bv_state00001"
        }

        try:
            async with async_timeout.timeout(10):
                session = self.hass.helpers.aiohttp_client.async_get_clientsession()
                response = await session.post(API_URL, json=payload, headers=headers)
                
                if response.status != 200:
                    raise UpdateFailed(f"Errore API: {response.status}")
                
                res_json = await response.json()
                
                if res_json.get("code") != "200":
                    _LOGGER.error("Errore nei dati XEV: %s", res_json.get("message"))
                
                return res_json.get("data")

        except Exception as err:
            raise UpdateFailed(f"Errore di comunicazione con XEV: {err}")