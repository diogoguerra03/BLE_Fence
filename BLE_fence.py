import asyncio
from bleak import BleakScanner
from playsound import playsound
import os

DISTANCE = 5  # Distância em metros para o alerta
ALERT_SOUND = os.path.join(os.path.dirname(__file__), "alert.mp3")  # Caminho para o som

def estimate_distance(rssi, tx_power=-59):
    if rssi == 0:
        return -1
    ratio = rssi * 1.0 / tx_power
    if ratio < 1.0:
        return ratio ** 10
    else:
        return 0.89976 * (ratio ** 7.7095) + 0.111

async def scan_device(target_mac):
    while True:
        devices = await BleakScanner.discover(return_adv=True)
        for address, (device, adv) in devices.items():
            if address.lower() == target_mac.lower():
                rssi = adv.rssi
                distance = estimate_distance(rssi)
                # print(f"Dispositivo encontrado! RSSI: {rssi} dBm -> Distância estimada: {distance:.2f} metros")
                if distance > DISTANCE:
                    print(f"Alerta! O Tojal está a fugir! Distância: {distance:.2f} metros")
                    playsound(ALERT_SOUND)
                break

mac_do_telemovel = "43:52:C4:21:0E:65" # Substitua pelo MAC do seu dispositivo

# Criar loop corretamente (compatível com Python 3.10+ e WinRT)
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
try:
    loop.run_until_complete(scan_device(mac_do_telemovel))
except KeyboardInterrupt:
    print("Parado pelo utilizador.")
finally:
    loop.close()
