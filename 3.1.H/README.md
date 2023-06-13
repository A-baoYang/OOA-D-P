# [3.1.H] 觀察者模式——Youtube 訂閱機制

> Author: @A-baoYang (jyabaodsda)

### Object Oriented Analysis

![](336-3.1.H-OOA.png)

### Object Oriented Design

![](336-3.1.H-OOD.png)

### Run 
```bash
cd code
python main.py
```

- Logging

```bash
[root] [INFO] - Youtube 頻道 PewDiePie 創立
[root] [INFO] - Youtube 頻道 水球軟體學院 創立
[root] [INFO] - 水球 用戶加入了 Youtube
[root] [INFO] - 火球 用戶加入了 Youtube
[root] [INFO] - C1M1S2 影片建立
[root] [INFO] - Hello guys 影片建立
[root] [INFO] - C1M1S3 影片建立
[root] [INFO] - Minecraft 影片建立
[root] [INFO] - 水球 訂閱了 PewDiePie
[root] [INFO] - 火球 訂閱了 PewDiePie
[root] [INFO] - 水球 訂閱了 水球軟體學院
[root] [INFO] - 火球 訂閱了 水球軟體學院
[root] [INFO] - 頻道 水球軟體學院 上架了一則新影片 C1M1S2
[root] [INFO] - 水球 對影片 "C1M1S2" 按讚。
[root] [INFO] - 頻道 PewDiePie 上架了一則新影片 Hello guys
[root] [INFO] - 火球 解除訂閱了 PewDiePie
[root] [INFO] - 頻道 水球軟體學院 上架了一則新影片 C1M1S3
[root] [INFO] - 火球 解除訂閱了 水球軟體學院
[root] [INFO] - 頻道 PewDiePie 上架了一則新影片 Minecraft
[root] [INFO] - 水球 對影片 "Minecraft" 按讚。
```

- OCP Logging

```bash
[root] [INFO] - Youtube 頻道 PewDiePie 創立
[root] [INFO] - Youtube 頻道 水球軟體學院 創立
[root] [INFO] - 水球 用戶加入了 Youtube
[root] [INFO] - 火球 用戶加入了 Youtube
[root] [INFO] - 難懂的用戶 用戶加入了 Youtube
[root] [INFO] - C1M1S2 影片建立
[root] [INFO] - Hello guys 影片建立
[root] [INFO] - C1M1S3 影片建立
[root] [INFO] - Minecraft 影片建立
[root] [INFO] - Minecraft PartII 影片建立
[root] [INFO] - 水球 訂閱了 PewDiePie
[root] [INFO] - 火球 訂閱了 PewDiePie
[root] [INFO] - 難懂的用戶 訂閱了 PewDiePie
[root] [INFO] - 水球 訂閱了 水球軟體學院
[root] [INFO] - 火球 訂閱了 水球軟體學院
[root] [INFO] - 難懂的用戶 訂閱了 水球軟體學院
[root] [INFO] - 頻道 水球軟體學院 上架了一則新影片 C1M1S2
[root] [INFO] - 水球 對影片 "C1M1S2" 按讚。
[root] [INFO] - 難懂的用戶 對影片 "C1M1S2" 按倒讚。
[root] [INFO] - 頻道 PewDiePie 上架了一則新影片 Hello guys
[root] [INFO] - 火球 解除訂閱了 PewDiePie
[root] [INFO] - 難懂的用戶 對影片 "Hello guys" 留言：「可以拍長一點的影片嗎」
[root] [INFO] - 頻道 水球軟體學院 上架了一則新影片 C1M1S3
[root] [INFO] - 火球 解除訂閱了 水球軟體學院
[root] [INFO] - 難懂的用戶 對影片 "C1M1S3" 留言：「可以拍長一點的影片嗎」
[root] [INFO] - 頻道 PewDiePie 上架了一則新影片 Minecraft
[root] [INFO] - 水球 對影片 "Minecraft" 按讚。
[root] [INFO] - 難懂的用戶 對影片 "Minecraft" 按讚。
[root] [INFO] - 頻道 PewDiePie 上架了一則新影片 Minecraft PartII
[root] [INFO] - 水球 對影片 "Minecraft PartII" 按讚。
[root] [INFO] - 難懂的用戶 對影片 "Minecraft PartII" 按讚。
[root] [INFO] - 難懂的用戶 解除訂閱了 PewDiePie
(
```