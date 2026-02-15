import uuid
import logging
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from .api import XevApi
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

class XevYoyoFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    
    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}
        if user_input is not None:
            try:
                generated_uuid = str(uuid.uuid4()).upper()
                session = async_get_clientsession(self.hass)
                
                api = XevApi(
                    session, 
                    user_input["mobile"], 
                    user_input["password"], 
                    user_input["region_code"],
                    generated_uuid
                )
                
                token, error_msg = await api.login() 
                
                if token:
                    vehicles = await api.get_vehicles(token)
                    if vehicles:
                        user_input["uuid"] = generated_uuid
                        user_input["vehicle_id"] = vehicles[0]["id"]
                        user_input["token"] = token
                        return self.async_create_entry(title="XEV Yoyo", data=user_input)
                    
                    errors["base"] = "no_vehicles"
                else:
                    errors["base"] = "invalid_auth"

            except Exception as e:
                _LOGGER.error("Errore durante il setup XEV: %s", e)
                errors["base"] = "cannot_connect"

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("region_code", default="39"): str,
                vol.Required("mobile"): str,
                vol.Required("password"): str,
            }),
            errors=errors
        )