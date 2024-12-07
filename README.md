# switch_control

## Hello World
```
python3 test/hello.py
```

## 実行
ペアリングと自動入力が実行される
```
sudo joycontrol-pluginloader -r 94:58:CB:64:5C:56 ../app/dragonquest3/RepeatXA.py
```

## ペアリング
```
sudo joycontrol-pluginloader plugins/tests/PairingController.py
```

## ゲームに戻る
不要
```
sudo joycontrol-pluginloader -r 94:58:CB:64:5C:56 switch_control/app/returnGame.py
```

## 接続できない場合

### 登録情報の削除
```
bluetoothctl paired-devices
bluetoothctl remove XX:XX:XX:XX:XX:XX
```

### 「KeyError: 'Name'」というエラー
```
sudo systemctl restart bluetooth.service
```