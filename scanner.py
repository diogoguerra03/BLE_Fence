import asyncio
from bleak import BleakScanner

async def main():
    print("A procurar dispositivos BLE...")
    devices = await BleakScanner.discover()
    for d in devices:
        print(f"Nome: {d.name}, MAC: {d.address}, RSSI: {d.rssi}")

asyncio.run(main())
