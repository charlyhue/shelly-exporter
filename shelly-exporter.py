import argparse
import confuse
import shelly
from prometheus_client import start_http_server, Gauge
import time
import asyncio


POWER_GAUGE = Gauge('shelly_power', 'Power consumption', ['device'])

parser = argparse.ArgumentParser(description='Shelly prometheus exporter.')
parser.add_argument('-c', '--config', default='config.yaml', help='Configuration file')
args = parser.parse_args()

config = confuse.YamlSource(args.config)


devices = []
for d in config['devices']:
    devices.append(getattr(shelly, d['type'])(d['ip']))

async def main():
    try:
        for d in devices:
            if isinstance(d, shelly.Plug):
                POWER_GAUGE.labels(device=d.getHostname()).set(d.getPower()['power'])
    except Exception as e:
        print("error")
        print(e)

if __name__ == "__main__":
    # Start up the server to expose the metrics.
    start_http_server(config['port'])
    # Generate some requests.
    while True:
        asyncio.run(main())
        time.sleep(config['interval'])
