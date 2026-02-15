from homeassistant.components.binary_sensor import (
    BinarySensorDeviceClass,
    BinarySensorEntity,
)
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from .const import DOMAIN

async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data[DOMAIN][entry.entry_id]
    
    async_add_entities([
        XevLockSensor(coordinator),
        XevWindowBinarySensor(coordinator),
    ])

class XevYoyoBinaryBase(CoordinatorEntity, BinarySensorEntity):
    _attr_has_entity_name = True

    def __init__(self, coordinator):
        super().__init__(coordinator)
        self.vehicle_id = coordinator.entry_data["vehicle_id"]

    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, self.vehicle_id)},
            "name": "XEV Yoyo",
            "manufacturer": "XEV",
            "model": "Yoyo",
        }

class XevLockSensor(XevYoyoBinaryBase):
    _attr_translation_key = "lock"
    _attr_device_class = BinarySensorDeviceClass.LOCK

    @property
    def unique_id(self):
        return f"{self.vehicle_id}_lock"

    @property
    def is_on(self):
        data = self.coordinator.data
        if data and "basic_info" in data:
            return data["basic_info"].get("door_status") == 0
        return None

class XevWindowBinarySensor(XevYoyoBinaryBase):
    _attr_translation_key = "windows"
    _attr_device_class = BinarySensorDeviceClass.WINDOW

    @property
    def unique_id(self):
        return f"{self.vehicle_id}_windows_binary"

    @property
    def is_on(self):
        data = self.coordinator.data
        if data and "basic_info" in data:
            return data["basic_info"].get("window_status") == 100
        return None