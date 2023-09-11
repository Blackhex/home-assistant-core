"""Constants for the Microsoft Teams Presence integration."""
import logging
from typing import Final

from homeassistant.const import Platform

DOMAIN: Final = "microsoft_teams_presence"
PLATFORMS: list[Platform] = [Platform.BINARY_SENSOR]

LOGGER = logging.getLogger(__package__)
