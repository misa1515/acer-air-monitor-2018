"""Binary sensor platform for acer_air_monitor."""
from homeassistant.components.binary_sensor import BinarySensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import BINARY_SENSOR, BINARY_SENSOR_DEVICE_CLASS, DEFAULT_NAME, DOMAIN
from .entity import IntegrationBlueprintEntity


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_devices):
    """Setup binary_sensor platform."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_devices([IntegrationBlueprintBinarySensor(coordinator, entry)])


class IntegrationBlueprintBinarySensor(IntegrationBlueprintEntity, BinarySensorEntity):
    """acer_air_monitor binary_sensor class."""

    @property
    def name(self):
        """Return the name of the binary_sensor."""
        return f"{DEFAULT_NAME}_{BINARY_SENSOR}"

    @property
    def device_class(self):
        """Return the class of this binary_sensor."""
        return BINARY_SENSOR_DEVICE_CLASS

    @property
    def is_on(self) -> bool:
        """Return true if the binary_sensor is on."""
        return self.coordinator.data.get("title", "") == "foo"
