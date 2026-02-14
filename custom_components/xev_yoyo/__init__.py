import logging
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, ServiceCall
from .coordinator import XevYoyoCoordinator
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

PLATFORMS = ["sensor", "device_tracker", "binary_sensor"]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    coordinator = XevYoyoCoordinator(hass, entry.data)
    
    await coordinator.async_config_entry_first_refresh()

    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = coordinator

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    async def handle_force_update(call: ServiceCall):
        _LOGGER.info("XEV Yoyo: Aggiornamento forzato richiesto dall'utente")
        await coordinator.async_refresh()

    hass.services.async_register(DOMAIN, "force_update", handle_force_update)
    
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok