import keyboard
import time
import pygame
import sys
import os

class KeyPressTracker:
  def __init__(self, key, count, within_seconds, sound_file):
        self.key = key
        self.count = count
        self.within_seconds = within_seconds
        self.sound_file = self.resource_path(sound_file)
        self.pressed_times = []

        pygame.mixer.init()

  def resource_path(self, relative_path):
      """ Get absolute path to resource, works for dev and for PyInstaller """
      try:
          # PyInstaller creates a temp folder and stores path in _MEIPASS
          base_path = sys._MEIPASS
      except Exception:
          base_path = os.path.abspath(".")

      return os.path.join(base_path, relative_path)

  def track(self, e):
    self.pressed_times.append(time.time())
    self.pressed_times = [t for t in self.pressed_times if time.time() - t <= self.within_seconds]

    if len(self.pressed_times) >= self.count:
      pygame.mixer.music.load(self.sound_file)
      pygame.mixer.music.play()
      print("Free Bird")
      time.sleep(10)
      pygame.mixer.music.stop()
      self.pressed_times.clear()

tracker = KeyPressTracker('e', 3, 0.4, 'free-bird.mp3')
keyboard.on_press_key(tracker.key, tracker.track)

# block forever
while True:
  time.sleep(1)