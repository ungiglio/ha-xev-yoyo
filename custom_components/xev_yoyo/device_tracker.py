from homeassistant.components.device_tracker import SourceType, TrackerEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from .const import DOMAIN

async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([XevYoyoTracker(coordinator)])

class XevYoyoTracker(CoordinatorEntity, TrackerEntity):
    
    _attr_has_entity_name = True
    _attr_translation_key = "location"

    def __init__(self, coordinator):
        super().__init__(coordinator)
        self.vehicle_id = coordinator.entry_data["vehicle_id"]
        self._attr_unique_id = f"{self.vehicle_id}_location"

    @property
    def source_type(self):
        return SourceType.GPS

    @property
    def latitude(self):
        data = self.coordinator.data
        if data and "basic_info" in data:
            return data["basic_info"].get("lat")
        return None

    @property
    def longitude(self):
        data = self.coordinator.data
        if data and "basic_info" in data:
            return data["basic_info"].get("lng")
        return None

    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, self.vehicle_id)},
            "name": "XEV Yoyo",
            "manufacturer": "XEV",
            "model": "Yoyo",
        }
        
    @property
    def icon(self):
        return "mdi:car"