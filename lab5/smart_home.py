"""Smart home device demo."""

import json
import subprocess
from pathlib import Path

HUB_HOST = "127.0.0.1"
HUB_PORT = 8080
POWER_USAGE = {"light": 10, "fan": 60, "thermostat": 1500, "tv": 120}
SCENE_DIR = Path(__file__).resolve().parent / "scenes"
devices = {}


def add_device(device_name, kind, room="Living Room", settings=None):
    """Add a device to the home."""
    device_settings = dict(settings) if settings is not None else {}
    if kind == "thermostat":
        device_settings.setdefault("temperature", 20)

    devices[device_name] = {
        "kind": kind,
        "room": room,
        "on": False,
        "settings": device_settings,
    }


def toggle_device(device_name):
    """Switch a device on or off."""
    device = devices.get(device_name)
    if device is None:
        print("Device not found:", device_name)
        return None

    device["on"] = not device["on"]
    return device["on"]


def set_temperature(device_name, value):
    """Set a thermostat temperature between 16 and 30."""
    device = devices.get(device_name)
    if device is None:
        print("Device not found:", device_name)
        return False
    if device["kind"] != "thermostat":
        print(device_name, "is not a thermostat")
        return False

    device["settings"]["temperature"] = min(max(value, 16), 30)
    return True


def devices_in_room(room):
    """List devices in a room."""
    return [name for name, info in devices.items() if info["room"] == room]


def power_usage():
    """Get the total power use of switched-on devices."""
    active = [info for info in devices.values() if info["on"]]
    return sum(POWER_USAGE.get(info["kind"], 0) for info in active)


def save_state(file_name="home_state.json"):
    """Save device details to a JSON file."""
    with open(file_name, "w", encoding="utf-8") as state_file:
        json.dump(devices, state_file, indent=2)


def hub_address():
    """Return the local hub address."""
    return HUB_HOST + ":" + str(HUB_PORT)


def run_scene(scene_script):
    """Run a scene script from the scenes folder."""
    scene_root = SCENE_DIR.resolve()
    scene_name = Path(scene_script)
    if scene_name.name != scene_script or scene_name.suffix != ".sh":
        print("Invalid scene script:", scene_script)
        return False

    scene_path = (scene_root / scene_name).resolve()
    if not scene_path.is_relative_to(scene_root) or not scene_path.is_file():
        print("Scene script not found or not allowed:", scene_script)
        return False

    try:
        result = subprocess.run(
            ["bash", str(scene_path)], check=False, shell=False
        )
    except OSError as error:
        print("Unable to run scene:", error)
        return False
    return result.returncode == 0


def main():
    """Run a short demo of the devices."""
    add_device("Ceiling Light", "light")
    add_device("Bedroom Fan", "fan", "Bedroom")
    add_device("Thermostat", "thermostat", "Bedroom")
    add_device("Smart TV", "tv")
    toggle_device("Ceiling Light")
    toggle_device("Thermostat")
    toggle_device("Garage Door")
    set_temperature("Thermostat", 35)
    set_temperature("Ceiling Light", 20)
    print("Bedroom devices:", devices_in_room("Bedroom"))
    print("Current power use (W):", power_usage())
    print("Hub address:", hub_address())
    print("Light settings:", devices["Ceiling Light"]["settings"])
    active_devices = [name for name, info in devices.items() if info["on"]]
    print("Devices on:", active_devices)
    save_state()


if __name__ == "__main__":
    main()
