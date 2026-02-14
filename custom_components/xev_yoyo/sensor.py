import logging
from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data[DOMAIN][entry.entry_id]

    sensors = [
        XevBatterySensor(coordinator),
        XevRangeSensor(coordinator),
        XevOdometerSensor(coordinator),
        XevStatusSensor(coordinator),
        XevDebugSensor(coordinator),
    ]

    async_add_entities(sensors)

class XevYoyoBaseSensor(CoordinatorEntity, SensorEntity):
    def __init__(self, coordinator):
        super().__init__(coordinator)
        self.vehicle_id = coordinator.entry_data["vehicle_id"]

    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, self.vehicle_id)},
            "name": "XEV Yoyo Pro",
            "manufacturer": "XEV",
            "model": "Yoyo Pro",
        }

class XevBatterySensor(XevYoyoBaseSensor):
    _attr_name = "XEV Yoyo Batteria"
    _attr_native_unit_of_measurement = "%"
    _attr_device_class = SensorDeviceClass.BATTERY
    _attr_state_class = SensorStateClass.MEASUREMENT

    @property
    def unique_id(self):
        return f"{self.vehicle_id}_battery"

    @property
    def native_value(self):
        data = self.coordinator.data
        if data and "charging_info" in data:
            return data["charging_info"].get("soc")
        return None

class XevRangeSensor(XevYoyoBaseSensor):
    _attr_name = "XEV Yoyo Autonomia"
    _attr_native_unit_of_measurement = "km"
    _attr_device_class = SensorDeviceClass.DISTANCE
    _attr_icon = "mdi:map-marker-distance"

    @property
    def unique_id(self):
        return f"{self.vehicle_id}_range"

    @property
    def native_value(self):
        data = self.coordinator.data
        if data and "charging_info" in data:
            return data["charging_info"].get("range_at_current_state")
        return None

class XevOdometerSensor(XevYoyoBaseSensor):
    _attr_name = "XEV Yoyo Contachilometri"
    _attr_native_unit_of_measurement = "km"
    _attr_device_class = SensorDeviceClass.DISTANCE
    _attr_state_class = SensorStateClass.TOTAL_INCREASING

    @property
    def unique_id(self):
        return f"{self.vehicle_id}_odometer"

    @property
    def native_value(self):
        data = self.coordinator.data
        if data and "basic_info" in data:
            return data["basic_info"].get("odometer")
        return None

class XevStatusSensor(XevYoyoBaseSensor):
    _attr_name = "XEV Yoyo Stato"

    @property
    def unique_id(self):
        return f"{self.vehicle_id}_status"

    @property
    def native_value(self):
        data = self.coordinator.data
        if data and "charging_info" in data:
            status = data["charging_info"].get("charging_status")
            if status == 1: return "In Carica"
            if status == 2: return "Disconnessa"
            return "Standby"
        return "Unknown"

class XevDebugSensor(XevYoyoBaseSensor):
    _attr_name = "XEV Yoyo API Debug"
    _attr_icon = "mdi:code-json"

    @property
    def unique_id(self):
        return f"{self.vehicle_id}_debug"

    @property
    def native_value(self):
        return "Online" if self.coordinator.data else "Offline"

    @property
    def extra_state_attributes(self):
        """Mette i dati grezzi qui."""
        return {"raw_data": self.coordinator.data}