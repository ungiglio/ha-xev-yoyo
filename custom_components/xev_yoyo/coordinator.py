import logging
from datetime import timedelta
import async_timeout

from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from .const import DOMAIN
from .api import XevApi

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
        session = async_get_clientsession(self.hass)
        api = XevApi(
            session, 
            self.entry_data["mobile"], 
            self.entry_data["password"], 
            self.entry_data.get("region_code"),
            self.entry_data["uuid"]
        )

        try:
            async with async_timeout.timeout(15):
                token = self.entry_data["token"]
                vehicle_id = self.entry_data["vehicle_id"]
                
                data = await api.get_vehicle_status(token, vehicle_id)
                
                if not data:
                    _LOGGER.info("XEV: Token scaduto, tento il re-login...")
                    new_token, error = await api.login()
                    if new_token:
                        self.entry_data["token"] = new_token
                        data = await api.get_vehicle_status(new_token, vehicle_id)
                    else:
                        raise UpdateFailed(f"Login fallito: {error}")

                if data:
                    return data
                
                raise UpdateFailed("Impossibile recuperare i dati del veicolo")

        except Exception as err:
            raise UpdateFailed(f"Errore aggiornamento: {err}")