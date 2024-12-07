#!/bin/bash

SCRIPT_DIR=$(cd $(dirname $0); pwd)

# cd $SCRIPT_DIR
# cd ../../joycontrol
# sudo python3 run_controller_cli.py PRO_CONTROLLER

cd $SCRIPT_DIR
cd ../../joycontrol-pluginloader
sudo joycontrol-pluginloader -r 94:58:CB:64:5C:56 ../app/returnGame.py

cd $SCRIPT_DIR
cd ../../joycontrol-pluginloader
sudo joycontrol-pluginloader -r 94:58:CB:64:5C:56 ../app/dragonquest3/RepeatXA.py