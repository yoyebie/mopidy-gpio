import logging
import traceback

from mopidy import core

import pykka

logger = logging.getLogger(__name__)


class GpioFrontend(pykka.ThreadingActor, core.CoreListener):

    def __init__(self, config, core):
        super(GpioFrontend, self).__init__()
        self.core = core
        
        from .gpio_output_manager import GPIOManager
        self.gpio_manager = GPIOManager(self, config['gpio'])

    def playback_state_changed(self, old_state, new_state):
        if new_state == core.PlaybackState.PLAYING:
            self.gpio_manager.set_led(True)
        else:
            self.gpio_manager.set_led(False)
