"""Constants for acer_air_monitor."""
# Base component constants
NAME = "Acer Air Monitor"
DOMAIN = "acer_air_monitor"
DOMAIN_DATA = f"{DOMAIN}_data"
VERSION = "0.0.1"
ATTRIBUTION = "Data provided by Acer Air Monitor"
ISSUE_URL = "https://github.com/sugoi-wada/acer-air-monitor-2018/issues"

# Icons
ICON = "mdi:format-quote-close"

# Device classes
BINARY_SENSOR_DEVICE_CLASS = "connectivity"

# Platforms
BINARY_SENSOR = "binary_sensor"
SENSOR = "sensor"
SWITCH = "switch"
PLATFORMS = [BINARY_SENSOR, SENSOR, SWITCH]


# Configuration and options
CONF_ENABLED = "enabled"
CONF_EMAIL = "email"
CONF_PASSWORD = "password"

USER_ATTR = "user_attr"

USER_ID = "aopUserId"

# Defaults
DEFAULT_NAME = DOMAIN


STARTUP_MESSAGE = f"""
-------------------------------------------------------------------
{NAME}
Version: {VERSION}
This is a custom integration!
If you have any issues with this you need to open an issue here:
{ISSUE_URL}
-------------------------------------------------------------------
"""
