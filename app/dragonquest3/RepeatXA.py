import logging
from JoycontrolPlugin import JoycontrolPlugin

logger = logging.getLogger(__name__)

class RepeatXA(JoycontrolPlugin):
    async def run(self):
        logger.info('Repeat X A Plugin')

        while True:
            await self.button_push('x')
            await self.wait(0.1)
            await self.button_push('a')
            await self.wait(0.1)