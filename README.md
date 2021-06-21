# Shelly-exporter
This is a prometheus exporter for shelly devices.

# Supported devices
- Shelly Plug S (tested)
- Shelly Plug (not tested)
- Shelly 1PM (not tested)

# Exported Metrics
## Plugs
- POWER_GAUGE: Current power consumption in Watt

# Installation
```bash
git clone https://github.com/charlyhue/shelly-exporter.git
cd shelly-exporter
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

# Configuration
See [example-config.yaml](https://github.com/charlyhue/shelly-exporter/blob/main/example-config.yml).

# Usage
### Command
```bash
python shelly-exporter.py -c config.yaml
```
### Systemd
```
[Unit]
Description=Shelly prometheus exporter

[Service]
ExecStart=/path/to/shelly-exporter/.venv/bin/python /path/to/shelly-exporter/shelly-exporter.py -c /path/to/shelly-exporter/config.yaml
User=prometheus
Group=prometheus

[Install]
WantedBy=multi-user.target
```