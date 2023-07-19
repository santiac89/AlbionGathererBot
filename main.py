
import threading
import argparse
from bot import Bot
from pynput import keyboard as kb
import scapy.all as scapy
from albion_events_handler import AlbionEventsHandler
from photon_packet_parser import PhotonPacketParser

from window_capture import WindowCapture
from detector import Detector
from keyboard_capture import KeyboardCapture

class EventsThread:
    def __init__(self, q):
        self._thread = None
        self._bot = bot
        self._lock = threading.Lock()
        self._stop_sniffing = False
        self._events_handler = AlbionEventsHandler(bot=self._bot)
        self._photon_packet_parser = PhotonPacketParser(on_event=self._events_handler.on_event, on_request=self._events_handler.on_request, on_response=self._events_handler.on_response)

    def handle_packet(self, packet):
        payload = packet.lastlayer().original
        self._photon_packet_parser.HandlePayload(payload=payload)

    def start(self):
        with self._lock:
            self._stop_sniffing = False
            self._thread = threading.Thread(target=self.run)
            self._thread.start()
    
    def stop (self):
        with self._lock:
            self._stop_sniffing = True
        
    def stop_filter(self, packet):
        with self._lock:
            return self._stop_sniffing

    def run(self):
        scapy.sniff(filter="(host 5.45.187 or host 5.188.125) and udp port 5056", prn=self.handle_packet, stop_filter=self.stop_filter)

models = {
    "1024": {
        "model_name": "1024_v7",
        "width": 1024,
        "height": 576,
        "shape": 1024
    },
    "640": {
        "model_name": "640_v2",
        "width": 1138,
        "height": 640,
        "shape": 640
    }
}

model = models["1024"]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                    prog='Albion Gatherer',
                    description='Bot to gather resources in Albion Online')

    parser.add_argument('-D', '--debug', type=bool, metavar='', default=False, required=False, help='Shows debug image')

    args = parser.parse_args()

    keyboard_thread = KeyboardCapture()
    window = WindowCapture("Albion Online Client")
    detector = Detector(model["model_name"], model["shape"])
    bot = Bot(window, detector)
    events_thread = EventsThread(bot)
    events_thread.start()
    
    def handle_key(key):
        if key == kb.KeyCode.from_char('s'):
            if bot.is_running():
                bot.stop()
            else:
                bot.start()
        elif key == kb.KeyCode.from_char('q'):
            print("Quitting...")
            events_thread.stop()
            keyboard_thread.stop()
            bot.stop()
            exit()

    keyboard_thread.on_key(handle_key)
    keyboard_thread.start()