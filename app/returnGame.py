# 持ち方順番を変える画面からゲームに戻る

import logging
from JoycontrolPlugin import JoycontrolPlugin

logger = logging.getLogger(__name__)

class returnGame(JoycontrolPlugin):
    async def run(self):
        logger.info('Return Game Plugin')

        # await self.wait(0.3)
        # await self.button_push('a')
        # logger.info('Push A buttons')
        # await self.wait(0.3)
        # await self.button_push('b')
        # logger.info('Push B buttons')
        # await self.wait(1)
        await self.button_push('home')
        logger.info('Push HOME buttons')