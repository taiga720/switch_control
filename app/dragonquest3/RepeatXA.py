import logging
from JoycontrolPlugin import JoycontrolPlugin

logger = logging.getLogger(__name__)

class RepeatXA(JoycontrolPlugin):
    async def run(self):
        logger.info('Repeat X A Plugin')

        while True:
            await self.button_push('x')
            logger.info('Repeat X Plugin')
            await self.wait(0.5)
            await self.button_push('a')
            logger.info('Repeat A1 Plugin')
            await self.wait(0.5)
            await self.button_push('a')
            logger.info('Repeat A2 Plugin')
            await self.wait(0.5)
            await self.button_push('a')
            logger.info('Repeat A3 Plugin')
            await self.wait(0.5)
            await self.button_push('a')
            logger.info('Repeat A4 Plugin')
            logger.info('Wait 10 Sec ...')
            await self.wait(10)
            await self.button_push('a')
            logger.info('Repeat A5 Plugin')
            await self.wait(0.5)
            await self.button_push('a')
            logger.info('Repeat A6 Plugin')
            await self.wait(0.5)