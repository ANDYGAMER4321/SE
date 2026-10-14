# Lab 5 Issues

Line numbers refer to the original `smart_home.py` file.

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---:|---|---|
| Unsafe shell command | Security, High (B602) | 49-51 | The function added the filename to a command and used `shell=True`. This could let extra commands run. | Check the filename and path, then use `subprocess.run` with `shell=False`. |
| Listening on all interfaces | Security, Medium (B104) | 4 | `0.0.0.0` listens on every network interface. | Changed it to `127.0.0.1` for local use. |
| Hard-coded password | Security, Low (B105) | 7 | A password-like value was in the code but was not used. | Removed the unused value. |
| Shared settings dictionary | Correctness (W0102) | 11-13 | Devices used the same default dictionary, so changing one device could affect others. | Give each device its own settings dictionary. |
| Inconsistent return value | Code quality (R1710) | 16-20 | The function returned a Boolean for a known device but nothing for an unknown one. | Return `None` when the device is not found. |
| Missing-device lookup | Robustness | 23-24 | An unknown device name could cause a `KeyError`. | Check that the device exists before changing its temperature. |
| Naming and missing docstrings | Code quality (C0103, C0114, C0116) | 1, 11-54 | Some names used camelCase and the functions had no docstrings. | Changed names to `snake_case` and added short docstrings. |
| File encoding | Portability (W1514) | 40-42 | The JSON file was opened without a set encoding. | Added `encoding="utf-8"`. |
| Formatting | Style (Flake8) | 6, 40, 66, 68 | The file had spacing, blank-line and line-length issues. | Fixed the formatting. |
