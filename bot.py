
import threading
import time
import pyautogui
import random
from PIL import ImageChops, Image
from resources_map import RESOURCES_MAP
from events.mount_event import MountEvent
from events.harvesting_finished_event import HarvestingFinishedEvent

from utils import Utils

class Resource:
    def __init__(self, name, box, distance):
        self.name = name
        self.box = box
        self.distance = distance

class Bot:
    def __init__(self, window, detector):
        self._window = window
        self._detector = detector
        self._pickIcon = Image.open("cursor.png").convert("RGB")
        self._player_position = (window.w / 2, window.h / 2)
        self._last_move_ts = 0
        self._last_harvest_finished_ts = 0
        self._last_harvest_started_ts = 0
        self._last_health_update_ts = 0
        self._is_harvesting = False
        self._harvest_lock = threading.Lock()
        self._mount_lock = threading.Lock()
        self._move_lock = threading.Lock()
        self._health_lock = threading.Lock()
        self._bot_lock = threading.Lock()
        self._is_mounted = False
        self._is_running = False

    def on_mount(self, event: MountEvent):
        with self._mount_lock:
            self._is_mounted = event.mounted

    def on_move(self, event):
        with self._move_lock:
            self._last_move_ts = time.time()

    def is_moving(self):
        with self._move_lock:
            return time.time() - self._last_move_ts < 2

    def on_harvest_finished(self, event: HarvestingFinishedEvent):
        with self._harvest_lock:
            if event.currentPossibleDegradationProcesses == 0:
                print("Harvest finished: ", RESOURCES_MAP[event.itemId])
                self._is_harvesting = False

            self._last_harvest_finished_ts = time.time()

    def on_harvest_started(self):
        with self._harvest_lock:
            self._is_harvesting = True
            self._last_harvest_started_ts = time.time()

    def is_harvesting(self):
        with self._harvest_lock:
            return self._is_harvesting 

    def on_health_update(self):
        with self._health_lock:
            self._last_health_update_ts = time.time()

    def is_being_hurt(self):
        with self._health_lock:
            return time.time() - self._last_health_update_ts < 2

    def scan_resources(self) -> list[Resource]:
        screenshot = self._window.get_screenshot()

        if screenshot is None:
            return []

        boxes, _, classes, _ = self._detector.detect(screenshot)

        resources = []

        for i in range(len(boxes)):
            x1, _, x2, y2 = boxes[i]
            object_middle_x = x1 + ((x2 - x1) / 2)
            distance = Utils.distance_between_points(p1=self._player_position, p2=(object_middle_x, y2))
            resources.append(Resource(self._detector.labels[int(classes[i])], boxes[i], distance))

        resources.sort(key=lambda x: x.distance)

        return resources

    def is_gather_cursor(self) -> bool:
        cursor, _ = self._window.get_cursor()
        diff = ImageChops.difference(cursor.convert("RGB"), self._pickIcon)
        return diff.getbbox() is None
 

    def get_random_direction(self):
        return random.choice([
            (self._player_position[0], self._player_position[1] - 400), # Up
            (self._player_position[0] + 400, self._player_position[1] - 400), # Up-Right
            (self._player_position[0] + 400, self._player_position[1]), # Right
            (self._player_position[0] + 400, self._player_position[1] + 400), # Down-Right
            (self._player_position[0], self._player_position[1] + 400), # Down
            (self._player_position[0] - 400, self._player_position[1] + 400), # Down-Left
            (self._player_position[0] - 400, self._player_position[1]), # Left
            (self._player_position[0] - 400, self._player_position[1] - 400) # Up-Left
        ])

    def search_gather_click_area(self, resource: Resource):
        x1, _, x2, y2 = resource.box
        x, y = x1, y2 - 20

        while self.is_gather_cursor() == False:
            pyautogui.moveTo(x, y)

            x += 10
            y -= 2

            if x >= x2:
                return False, 0, 0

        return True, x, y

    def is_running(self):
        with self._bot_lock:
            return self._is_running

    def stop(self):
        with self._bot_lock:
            self._is_running = False

    def start(self):
        with self._bot_lock:
            print("Starting bot")
            self._is_running = True
            self._thread = threading.Thread(target=self.run)
            self._thread.start()

    def wait_is_mounted(self, value):
        while True:
            with self._mount_lock:
                if self._is_mounted == value:
                    break

    def wait_is_moving(self, value):
        while True:
            if self.is_moving() == value:
                break

    def run(self):
        while True:
            with self._bot_lock:
                if self._is_running == False:
                    print("Stopping bot")
                    break

            if self.is_being_hurt():
                self._is_harvesting = False
                pyautogui.moveTo(self._player_position[0], self._player_position[1])
                pyautogui.press('space')
                pyautogui.press('w')
                pyautogui.press('e')
                continue

            if self._is_harvesting or self.is_moving():
                continue
            elif self._is_mounted == False:
                pyautogui.press('a')
                self.wait_is_mounted(True)

            nearby_resources = self.scan_resources()

            if len(nearby_resources) == 0: # NOTE: Improve look around logic
                x, y = self.get_random_direction()
                pyautogui.click(x, y)
                self.wait_is_moving(False)
                continue

            closest_resource = nearby_resources[0]

            print("Closest resource: " + closest_resource.name, " Distance: ", closest_resource.distance)

            if closest_resource.distance < 200: 
                found, x, y = self.search_gather_click_area(closest_resource) # NOTE: Bug here

                if found:
                    pyautogui.click(x, y)
            
            if closest_resource.distance >= 200 or found == False:
                x1, y1, x2, y2 = closest_resource.box
                object_corners = [(x1, y2),(x2, y2)]

                (x, y) = Utils.calculate_closest_point(self._player_position, object_corners)

                (player_x, player_y) = self._player_position

                if x < player_x:
                    x += 50
                else:
                    x -= 50

                if y < player_y:
                    y += 50
                else:
                    y -= 50

                pyautogui.click(x, y)