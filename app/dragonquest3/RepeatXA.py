import logging
from JoycontrolPlugin import JoycontrolPlugin
import time

logger = logging.getLogger(__name__)

class RepeatXA(JoycontrolPlugin):
    async def run(self):
        logger.info('Repeat X A Plugin')

        start = 0 # xボタン押下後計測開始時間
        end = 30   # xボタン押下後経過時間
        while True:
            # xボタン長押し後30秒はxとaボタン連打
            # → たまに逃げるループから抜けるため
            if end - start >= 20 :

                # 逃げるためxボタン長押し
                logger.info('Push X Button')
                await self.button_press('x')
                await self.wait(3)
                await self.button_release('x')

                # xボタン押下後計測開始時間
                start = time.perf_counter()

            else:
                await self.button_push('a')
                logger.info('Push A Button')
                await self.wait(0.3)

                # xボタン押下後経過時間
                end = time.perf_counter()