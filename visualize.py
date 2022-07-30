import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

text = """
Epoch 1/200
10/10 [==============================] - 9s 499ms/step - loss: 0.2671 - acc: 0.9147 - val_loss: 0.2525 - val_acc: 0.9170
Epoch 2/200
10/10 [==============================] - 4s 380ms/step - loss: 0.2381 - acc: 0.9227 - val_loss: 0.2412 - val_acc: 0.9209
Epoch 3/200
10/10 [==============================] - 4s 382ms/step - loss: 0.2286 - acc: 0.9255 - val_loss: 0.2342 - val_acc: 0.9234
Epoch 4/200
10/10 [==============================] - 4s 406ms/step - loss: 0.2251 - acc: 0.9267 - val_loss: 0.2303 - val_acc: 0.9242
Epoch 5/200
10/10 [==============================] - 4s 379ms/step - loss: 0.2187 - acc: 0.9285 - val_loss: 0.2266 - val_acc: 0.9254
Epoch 6/200
10/10 [==============================] - 4s 376ms/step - loss: 0.2157 - acc: 0.9296 - val_loss: 0.2251 - val_acc: 0.9256
Epoch 7/200
10/10 [==============================] - 4s 379ms/step - loss: 0.2148 - acc: 0.9294 - val_loss: 0.2248 - val_acc: 0.9259
Epoch 8/200
10/10 [==============================] - 4s 407ms/step - loss: 0.2128 - acc: 0.9301 - val_loss: 0.2197 - val_acc: 0.9279
Epoch 9/200
10/10 [==============================] - 4s 406ms/step - loss: 0.2105 - acc: 0.9310 - val_loss: 0.2182 - val_acc: 0.9274
Epoch 10/200
10/10 [==============================] - 4s 377ms/step - loss: 0.2092 - acc: 0.9312 - val_loss: 0.2192 - val_acc: 0.9270
Epoch 11/200
10/10 [==============================] - 4s 381ms/step - loss: 0.2069 - acc: 0.9318 - val_loss: 0.2158 - val_acc: 0.9286
Epoch 12/200
10/10 [==============================] - 4s 377ms/step - loss: 0.2061 - acc: 0.9323 - val_loss: 0.2201 - val_acc: 0.9278
Epoch 13/200
10/10 [==============================] - 4s 376ms/step - loss: 0.2093 - acc: 0.9311 - val_loss: 0.2168 - val_acc: 0.9279
Epoch 14/200
10/10 [==============================] - 4s 378ms/step - loss: 0.2064 - acc: 0.9321 - val_loss: 0.2158 - val_acc: 0.9282
Epoch 15/200
10/10 [==============================] - 4s 378ms/step - loss: 0.2023 - acc: 0.9332 - val_loss: 0.2130 - val_acc: 0.9287
Epoch 16/200
10/10 [==============================] - 4s 376ms/step - loss: 0.2015 - acc: 0.9336 - val_loss: 0.2177 - val_acc: 0.9286
Epoch 17/200
10/10 [==============================] - 4s 379ms/step - loss: 0.2013 - acc: 0.9339 - val_loss: 0.2121 - val_acc: 0.9291
Epoch 18/200
10/10 [==============================] - 4s 377ms/step - loss: 0.2052 - acc: 0.9323 - val_loss: 0.2134 - val_acc: 0.9283
Epoch 19/200
10/10 [==============================] - 4s 378ms/step - loss: 0.2019 - acc: 0.9332 - val_loss: 0.2109 - val_acc: 0.9299
Epoch 20/200
10/10 [==============================] - 4s 403ms/step - loss: 0.1995 - acc: 0.9343 - val_loss: 0.2067 - val_acc: 0.9318
Epoch 21/200
10/10 [==============================] - 4s 376ms/step - loss: 0.1956 - acc: 0.9356 - val_loss: 0.2051 - val_acc: 0.9313
Epoch 22/200
10/10 [==============================] - 4s 404ms/step - loss: 0.1948 - acc: 0.9357 - val_loss: 0.2036 - val_acc: 0.9323
Epoch 23/200
10/10 [==============================] - 4s 378ms/step - loss: 0.1905 - acc: 0.9375 - val_loss: 0.2030 - val_acc: 0.9327
Epoch 24/200
10/10 [==============================] - 4s 377ms/step - loss: 0.1916 - acc: 0.9370 - val_loss: 0.2008 - val_acc: 0.9326
Epoch 25/200
10/10 [==============================] - 4s 378ms/step - loss: 0.1895 - acc: 0.9378 - val_loss: 0.2007 - val_acc: 0.9332
Epoch 26/200
10/10 [==============================] - 4s 407ms/step - loss: 0.1877 - acc: 0.9382 - val_loss: 0.1966 - val_acc: 0.9347
Epoch 27/200
10/10 [==============================] - 4s 376ms/step - loss: 0.1851 - acc: 0.9393 - val_loss: 0.1972 - val_acc: 0.9345
Epoch 28/200
10/10 [==============================] - 4s 378ms/step - loss: 0.1864 - acc: 0.9387 - val_loss: 0.1969 - val_acc: 0.9350
Epoch 29/200
10/10 [==============================] - 4s 376ms/step - loss: 0.1860 - acc: 0.9388 - val_loss: 0.1959 - val_acc: 0.9347
Epoch 30/200
10/10 [==============================] - 4s 375ms/step - loss: 0.1834 - acc: 0.9397 - val_loss: 0.1952 - val_acc: 0.9351
Epoch 31/200
10/10 [==============================] - 4s 378ms/step - loss: 0.1836 - acc: 0.9395 - val_loss: 0.1948 - val_acc: 0.9351
Epoch 32/200
10/10 [==============================] - 4s 376ms/step - loss: 0.1841 - acc: 0.9395 - val_loss: 0.1960 - val_acc: 0.9342
Epoch 33/200
10/10 [==============================] - 4s 377ms/step - loss: 0.1831 - acc: 0.9396 - val_loss: 0.1934 - val_acc: 0.9356
Epoch 34/200
10/10 [==============================] - 4s 378ms/step - loss: 0.1800 - acc: 0.9411 - val_loss: 0.1911 - val_acc: 0.9366
Epoch 35/200
10/10 [==============================] - 4s 379ms/step - loss: 0.1784 - acc: 0.9416 - val_loss: 0.1909 - val_acc: 0.9367
Epoch 36/200
10/10 [==============================] - 4s 405ms/step - loss: 0.1765 - acc: 0.9418 - val_loss: 0.1876 - val_acc: 0.9382
Epoch 37/200
10/10 [==============================] - 4s 379ms/step - loss: 0.1769 - acc: 0.9419 - val_loss: 0.1887 - val_acc: 0.9371
Epoch 38/200
10/10 [==============================] - 4s 380ms/step - loss: 0.1773 - acc: 0.9416 - val_loss: 0.1920 - val_acc: 0.9362
Epoch 39/200
10/10 [==============================] - 4s 378ms/step - loss: 0.1779 - acc: 0.9417 - val_loss: 0.1887 - val_acc: 0.9371
Epoch 40/200
10/10 [==============================] - 4s 379ms/step - loss: 0.1733 - acc: 0.9430 - val_loss: 0.1853 - val_acc: 0.9386
Epoch 41/200
10/10 [==============================] - 4s 379ms/step - loss: 0.1740 - acc: 0.9430 - val_loss: 0.1854 - val_acc: 0.9390
Epoch 42/200
10/10 [==============================] - 4s 407ms/step - loss: 0.1698 - acc: 0.9445 - val_loss: 0.1815 - val_acc: 0.9402
Epoch 43/200
10/10 [==============================] - 4s 376ms/step - loss: 0.1680 - acc: 0.9453 - val_loss: 0.1800 - val_acc: 0.9406
Epoch 44/200
10/10 [==============================] - 4s 407ms/step - loss: 0.1657 - acc: 0.9460 - val_loss: 0.1787 - val_acc: 0.9411
Epoch 45/200
10/10 [==============================] - 4s 378ms/step - loss: 0.1652 - acc: 0.9462 - val_loss: 0.1778 - val_acc: 0.9409
Epoch 46/200
10/10 [==============================] - 4s 405ms/step - loss: 0.1674 - acc: 0.9449 - val_loss: 0.1801 - val_acc: 0.9402
Epoch 47/200
10/10 [==============================] - 4s 379ms/step - loss: 0.1687 - acc: 0.9444 - val_loss: 0.1824 - val_acc: 0.9389
Epoch 48/200
10/10 [==============================] - 4s 376ms/step - loss: 0.1658 - acc: 0.9457 - val_loss: 0.1781 - val_acc: 0.9411
Epoch 49/200
10/10 [==============================] - 4s 379ms/step - loss: 0.1650 - acc: 0.9458 - val_loss: 0.1788 - val_acc: 0.9404
Epoch 50/200
10/10 [==============================] - 4s 378ms/step - loss: 0.1633 - acc: 0.9466 - val_loss: 0.1762 - val_acc: 0.9416
Epoch 51/200
10/10 [==============================] - 4s 377ms/step - loss: 0.1603 - acc: 0.9475 - val_loss: 0.1739 - val_acc: 0.9422
Epoch 52/200
10/10 [==============================] - 4s 379ms/step - loss: 0.1582 - acc: 0.9485 - val_loss: 0.1726 - val_acc: 0.9424
Epoch 53/200
10/10 [==============================] - 4s 379ms/step - loss: 0.1568 - acc: 0.9489 - val_loss: 0.1728 - val_acc: 0.9429
Epoch 54/200
10/10 [==============================] - 4s 376ms/step - loss: 0.1568 - acc: 0.9487 - val_loss: 0.1737 - val_acc: 0.9430
Epoch 55/200
10/10 [==============================] - 4s 378ms/step - loss: 0.1562 - acc: 0.9491 - val_loss: 0.1716 - val_acc: 0.9430
Epoch 56/200
10/10 [==============================] - 4s 377ms/step - loss: 0.1552 - acc: 0.9493 - val_loss: 0.1718 - val_acc: 0.9434
Epoch 57/200
10/10 [==============================] - 4s 378ms/step - loss: 0.1549 - acc: 0.9492 - val_loss: 0.1693 - val_acc: 0.9441
Epoch 58/200
10/10 [==============================] - 4s 378ms/step - loss: 0.1546 - acc: 0.9494 - val_loss: 0.1691 - val_acc: 0.9442
Epoch 59/200
10/10 [==============================] - 4s 377ms/step - loss: 0.1522 - acc: 0.9503 - val_loss: 0.1682 - val_acc: 0.9443
Epoch 60/200
10/10 [==============================] - 4s 380ms/step - loss: 0.1520 - acc: 0.9502 - val_loss: 0.1683 - val_acc: 0.9446
Epoch 61/200
10/10 [==============================] - 4s 405ms/step - loss: 0.1558 - acc: 0.9488 - val_loss: 0.1703 - val_acc: 0.9433
Epoch 62/200
10/10 [==============================] - 4s 378ms/step - loss: 0.1517 - acc: 0.9505 - val_loss: 0.1675 - val_acc: 0.9447
Epoch 63/200
10/10 [==============================] - 4s 377ms/step - loss: 0.1495 - acc: 0.9509 - val_loss: 0.1657 - val_acc: 0.9449
Epoch 64/200
10/10 [==============================] - 4s 376ms/step - loss: 0.1478 - acc: 0.9517 - val_loss: 0.1654 - val_acc: 0.9450
Epoch 65/200
10/10 [==============================] - 4s 377ms/step - loss: 0.1490 - acc: 0.9512 - val_loss: 0.1639 - val_acc: 0.9456
Epoch 66/200
10/10 [==============================] - 4s 375ms/step - loss: 0.1488 - acc: 0.9514 - val_loss: 0.1667 - val_acc: 0.9454
Epoch 67/200
10/10 [==============================] - 4s 406ms/step - loss: 0.1460 - acc: 0.9523 - val_loss: 0.1621 - val_acc: 0.9464
Epoch 68/200
10/10 [==============================] - 4s 377ms/step - loss: 0.1444 - acc: 0.9530 - val_loss: 0.1606 - val_acc: 0.9465
Epoch 69/200
10/10 [==============================] - 4s 375ms/step - loss: 0.1418 - acc: 0.9538 - val_loss: 0.1617 - val_acc: 0.9464
Epoch 70/200
10/10 [==============================] - 4s 375ms/step - loss: 0.1435 - acc: 0.9531 - val_loss: 0.1615 - val_acc: 0.9469
Epoch 71/200
10/10 [==============================] - 4s 379ms/step - loss: 0.1419 - acc: 0.9536 - val_loss: 0.1609 - val_acc: 0.9466
Epoch 72/200
10/10 [==============================] - 4s 380ms/step - loss: 0.1402 - acc: 0.9543 - val_loss: 0.1600 - val_acc: 0.9467
Epoch 73/200
10/10 [==============================] - 4s 376ms/step - loss: 0.1405 - acc: 0.9541 - val_loss: 0.1608 - val_acc: 0.9471
Epoch 74/200
10/10 [==============================] - 4s 376ms/step - loss: 0.1407 - acc: 0.9540 - val_loss: 0.1598 - val_acc: 0.9475
Epoch 75/200
10/10 [==============================] - 4s 381ms/step - loss: 0.1381 - acc: 0.9548 - val_loss: 0.1599 - val_acc: 0.9473
Epoch 76/200
10/10 [==============================] - 4s 377ms/step - loss: 0.1441 - acc: 0.9526 - val_loss: 0.1602 - val_acc: 0.9471
Epoch 77/200
10/10 [==============================] - 4s 378ms/step - loss: 0.1420 - acc: 0.9532 - val_loss: 0.1603 - val_acc: 0.9472
Epoch 78/200
10/10 [==============================] - 4s 376ms/step - loss: 0.1393 - acc: 0.9545 - val_loss: 0.1585 - val_acc: 0.9475
Epoch 79/200
10/10 [==============================] - 4s 379ms/step - loss: 0.1382 - acc: 0.9547 - val_loss: 0.1572 - val_acc: 0.9481
Epoch 80/200
10/10 [==============================] - 4s 378ms/step - loss: 0.1361 - acc: 0.9553 - val_loss: 0.1594 - val_acc: 0.9468
Epoch 81/200
10/10 [==============================] - 4s 378ms/step - loss: 0.1355 - acc: 0.9555 - val_loss: 0.1548 - val_acc: 0.9487
Epoch 82/200
10/10 [==============================] - 4s 379ms/step - loss: 0.1327 - acc: 0.9567 - val_loss: 0.1551 - val_acc: 0.9489
Epoch 83/200
10/10 [==============================] - 4s 378ms/step - loss: 0.1350 - acc: 0.9558 - val_loss: 0.1555 - val_acc: 0.9484
Epoch 84/200
10/10 [==============================] - 4s 378ms/step - loss: 0.1338 - acc: 0.9561 - val_loss: 0.1546 - val_acc: 0.9486
Epoch 85/200
10/10 [==============================] - 4s 378ms/step - loss: 0.1319 - acc: 0.9569 - val_loss: 0.1531 - val_acc: 0.9494
Epoch 86/200
10/10 [==============================] - 4s 376ms/step - loss: 0.1296 - acc: 0.9576 - val_loss: 0.1528 - val_acc: 0.9492
Epoch 87/200
10/10 [==============================] - 4s 377ms/step - loss: 0.1315 - acc: 0.9568 - val_loss: 0.1529 - val_acc: 0.9488
Epoch 88/200
10/10 [==============================] - 4s 380ms/step - loss: 0.1294 - acc: 0.9578 - val_loss: 0.1528 - val_acc: 0.9491
Epoch 89/200
10/10 [==============================] - 4s 376ms/step - loss: 0.1301 - acc: 0.9575 - val_loss: 0.1525 - val_acc: 0.9499
Epoch 90/200
10/10 [==============================] - 4s 378ms/step - loss: 0.1289 - acc: 0.9577 - val_loss: 0.1520 - val_acc: 0.9494
Epoch 91/200
10/10 [==============================] - 4s 376ms/step - loss: 0.1285 - acc: 0.9579 - val_loss: 0.1514 - val_acc: 0.9496
Epoch 92/200
10/10 [==============================] - 4s 378ms/step - loss: 0.1268 - acc: 0.9583 - val_loss: 0.1516 - val_acc: 0.9497
Epoch 93/200
10/10 [==============================] - 4s 379ms/step - loss: 0.1268 - acc: 0.9584 - val_loss: 0.1523 - val_acc: 0.9496
Epoch 94/200
10/10 [==============================] - 4s 405ms/step - loss: 0.1253 - acc: 0.9589 - val_loss: 0.1489 - val_acc: 0.9506
Epoch 95/200
10/10 [==============================] - 4s 376ms/step - loss: 0.1239 - acc: 0.9596 - val_loss: 0.1488 - val_acc: 0.9506
Epoch 96/200
10/10 [==============================] - 4s 381ms/step - loss: 0.1231 - acc: 0.9597 - val_loss: 0.1487 - val_acc: 0.9507
Epoch 97/200
10/10 [==============================] - 4s 380ms/step - loss: 0.1221 - acc: 0.9601 - val_loss: 0.1497 - val_acc: 0.9510
Epoch 98/200
10/10 [==============================] - 4s 407ms/step - loss: 0.1218 - acc: 0.9602 - val_loss: 0.1475 - val_acc: 0.9513
Epoch 99/200
10/10 [==============================] - 4s 378ms/step - loss: 0.1216 - acc: 0.9603 - val_loss: 0.1492 - val_acc: 0.9507
Epoch 100/200
10/10 [==============================] - 4s 396ms/step - loss: 0.1215 - acc: 0.9601 - val_loss: 0.1490 - val_acc: 0.9509
Epoch 101/200
10/10 [==============================] - 4s 378ms/step - loss: 0.1233 - acc: 0.9596 - val_loss: 0.1508 - val_acc: 0.9502
Epoch 102/200
10/10 [==============================] - 4s 379ms/step - loss: 0.1239 - acc: 0.9590 - val_loss: 0.1493 - val_acc: 0.9503
Epoch 103/200
10/10 [==============================] - 4s 379ms/step - loss: 0.1240 - acc: 0.9590 - val_loss: 0.1509 - val_acc: 0.9501
Epoch 104/200
10/10 [==============================] - 4s 377ms/step - loss: 0.1224 - acc: 0.9597 - val_loss: 0.1502 - val_acc: 0.9501
Epoch 105/200
10/10 [==============================] - 4s 382ms/step - loss: 0.1207 - acc: 0.9605 - val_loss: 0.1534 - val_acc: 0.9492
Epoch 106/200
10/10 [==============================] - 4s 377ms/step - loss: 0.1261 - acc: 0.9583 - val_loss: 0.1484 - val_acc: 0.9510
Epoch 107/200
10/10 [==============================] - 4s 377ms/step - loss: 0.1238 - acc: 0.9592 - val_loss: 0.1530 - val_acc: 0.9501
Epoch 108/200
10/10 [==============================] - 4s 379ms/step - loss: 0.1266 - acc: 0.9581 - val_loss: 0.1534 - val_acc: 0.9496
Epoch 109/200
10/10 [==============================] - 4s 405ms/step - loss: 0.1243 - acc: 0.9589 - val_loss: 0.1483 - val_acc: 0.9509
Epoch 110/200
10/10 [==============================] - 4s 379ms/step - loss: 0.1200 - acc: 0.9606 - val_loss: 0.1470 - val_acc: 0.9514
Epoch 111/200
10/10 [==============================] - 4s 378ms/step - loss: 0.1188 - acc: 0.9610 - val_loss: 0.1469 - val_acc: 0.9519
Epoch 112/200
10/10 [==============================] - 4s 377ms/step - loss: 0.1185 - acc: 0.9610 - val_loss: 0.1466 - val_acc: 0.9520
Epoch 113/200
10/10 [==============================] - 4s 379ms/step - loss: 0.1156 - acc: 0.9622 - val_loss: 0.1451 - val_acc: 0.9521
Epoch 114/200
10/10 [==============================] - 4s 382ms/step - loss: 0.1144 - acc: 0.9626 - val_loss: 0.1451 - val_acc: 0.9524
Epoch 115/200
10/10 [==============================] - 4s 407ms/step - loss: 0.1130 - acc: 0.9632 - val_loss: 0.1444 - val_acc: 0.9523
Epoch 116/200
10/10 [==============================] - 4s 377ms/step - loss: 0.1119 - acc: 0.9636 - val_loss: 0.1437 - val_acc: 0.9523
Epoch 117/200
10/10 [==============================] - 4s 379ms/step - loss: 0.1121 - acc: 0.9633 - val_loss: 0.1449 - val_acc: 0.9524
Epoch 118/200
10/10 [==============================] - 4s 408ms/step - loss: 0.1154 - acc: 0.9622 - val_loss: 0.1465 - val_acc: 0.9524
Epoch 119/200
10/10 [==============================] - 4s 377ms/step - loss: 0.1125 - acc: 0.9632 - val_loss: 0.1437 - val_acc: 0.9531
Epoch 120/200
10/10 [==============================] - 4s 376ms/step - loss: 0.1107 - acc: 0.9638 - val_loss: 0.1442 - val_acc: 0.9529
Epoch 121/200
10/10 [==============================] - 4s 377ms/step - loss: 0.1122 - acc: 0.9631 - val_loss: 0.1445 - val_acc: 0.9534
Epoch 122/200
10/10 [==============================] - 4s 376ms/step - loss: 0.1094 - acc: 0.9643 - val_loss: 0.1420 - val_acc: 0.9532
Epoch 123/200
10/10 [==============================] - 4s 379ms/step - loss: 0.1096 - acc: 0.9640 - val_loss: 0.1420 - val_acc: 0.9535
Epoch 124/200
10/10 [==============================] - 4s 378ms/step - loss: 0.1077 - acc: 0.9648 - val_loss: 0.1468 - val_acc: 0.9516
Epoch 125/200
10/10 [==============================] - 4s 379ms/step - loss: 0.1096 - acc: 0.9640 - val_loss: 0.1431 - val_acc: 0.9532
Epoch 126/200
10/10 [==============================] - 4s 377ms/step - loss: 0.1084 - acc: 0.9647 - val_loss: 0.1437 - val_acc: 0.9531
Epoch 127/200
10/10 [==============================] - 4s 406ms/step - loss: 0.1079 - acc: 0.9646 - val_loss: 0.1419 - val_acc: 0.9538
Epoch 128/200
10/10 [==============================] - 4s 380ms/step - loss: 0.1050 - acc: 0.9658 - val_loss: 0.1413 - val_acc: 0.9540
Epoch 129/200
10/10 [==============================] - 4s 405ms/step - loss: 0.1054 - acc: 0.9659 - val_loss: 0.1410 - val_acc: 0.9542
Epoch 130/200
10/10 [==============================] - 4s 378ms/step - loss: 0.1031 - acc: 0.9666 - val_loss: 0.1414 - val_acc: 0.9538
Epoch 131/200
10/10 [==============================] - 4s 381ms/step - loss: 0.1051 - acc: 0.9655 - val_loss: 0.1420 - val_acc: 0.9529
Epoch 132/200
10/10 [==============================] - 4s 379ms/step - loss: 0.1043 - acc: 0.9659 - val_loss: 0.1428 - val_acc: 0.9534
Epoch 133/200
10/10 [==============================] - 4s 377ms/step - loss: 0.1091 - acc: 0.9640 - val_loss: 0.1454 - val_acc: 0.9523
Epoch 134/200
10/10 [==============================] - 4s 376ms/step - loss: 0.1063 - acc: 0.9651 - val_loss: 0.1420 - val_acc: 0.9539
Epoch 135/200
10/10 [==============================] - 4s 408ms/step - loss: 0.1041 - acc: 0.9659 - val_loss: 0.1415 - val_acc: 0.9540
Epoch 136/200
10/10 [==============================] - 4s 406ms/step - loss: 0.1018 - acc: 0.9668 - val_loss: 0.1395 - val_acc: 0.9547
Epoch 137/200
10/10 [==============================] - 4s 377ms/step - loss: 0.1003 - acc: 0.9677 - val_loss: 0.1395 - val_acc: 0.9547
Epoch 138/200
10/10 [==============================] - 4s 407ms/step - loss: 0.0996 - acc: 0.9678 - val_loss: 0.1389 - val_acc: 0.9553
Epoch 139/200
10/10 [==============================] - 4s 378ms/step - loss: 0.0985 - acc: 0.9682 - val_loss: 0.1400 - val_acc: 0.9549
Epoch 140/200
10/10 [==============================] - 4s 380ms/step - loss: 0.0985 - acc: 0.9681 - val_loss: 0.1398 - val_acc: 0.9549
Epoch 141/200
10/10 [==============================] - 4s 377ms/step - loss: 0.0985 - acc: 0.9681 - val_loss: 0.1409 - val_acc: 0.9545
Epoch 142/200
10/10 [==============================] - 4s 379ms/step - loss: 0.0977 - acc: 0.9682 - val_loss: 0.1397 - val_acc: 0.9549
Epoch 143/200
10/10 [==============================] - 4s 396ms/step - loss: 0.1005 - acc: 0.9670 - val_loss: 0.1440 - val_acc: 0.9530
Epoch 144/200
10/10 [==============================] - 4s 377ms/step - loss: 0.1056 - acc: 0.9649 - val_loss: 0.1453 - val_acc: 0.9524
Epoch 145/200
10/10 [==============================] - 4s 378ms/step - loss: 0.1042 - acc: 0.9655 - val_loss: 0.1430 - val_acc: 0.9537
Epoch 146/200
10/10 [==============================] - 4s 408ms/step - loss: 0.1014 - acc: 0.9667 - val_loss: 0.1402 - val_acc: 0.9546
Epoch 147/200
10/10 [==============================] - 4s 382ms/step - loss: 0.0983 - acc: 0.9679 - val_loss: 0.1413 - val_acc: 0.9544
Epoch 148/200
10/10 [==============================] - 4s 377ms/step - loss: 0.0972 - acc: 0.9683 - val_loss: 0.1387 - val_acc: 0.9554
Epoch 149/200
10/10 [==============================] - 4s 376ms/step - loss: 0.0955 - acc: 0.9690 - val_loss: 0.1400 - val_acc: 0.9546
Epoch 150/200
10/10 [==============================] - 4s 378ms/step - loss: 0.0949 - acc: 0.9691 - val_loss: 0.1398 - val_acc: 0.9547
Epoch 151/200
10/10 [==============================] - 4s 405ms/step - loss: 0.0938 - acc: 0.9697 - val_loss: 0.1374 - val_acc: 0.9559
Epoch 152/200
10/10 [==============================] - 4s 378ms/step - loss: 0.0931 - acc: 0.9699 - val_loss: 0.1387 - val_acc: 0.9559
Epoch 153/200
10/10 [==============================] - 4s 379ms/step - loss: 0.0929 - acc: 0.9699 - val_loss: 0.1396 - val_acc: 0.9551
Epoch 154/200
10/10 [==============================] - 4s 383ms/step - loss: 0.0936 - acc: 0.9696 - val_loss: 0.1384 - val_acc: 0.9556
Epoch 155/200
10/10 [==============================] - 4s 376ms/step - loss: 0.0930 - acc: 0.9698 - val_loss: 0.1417 - val_acc: 0.9548
Epoch 156/200
10/10 [==============================] - 4s 376ms/step - loss: 0.0931 - acc: 0.9697 - val_loss: 0.1410 - val_acc: 0.9542
Epoch 157/200
10/10 [==============================] - 4s 381ms/step - loss: 0.0926 - acc: 0.9700 - val_loss: 0.1430 - val_acc: 0.9539
Epoch 158/200
10/10 [==============================] - 4s 378ms/step - loss: 0.1037 - acc: 0.9652 - val_loss: 0.1430 - val_acc: 0.9544
Epoch 159/200
10/10 [==============================] - 4s 407ms/step - loss: 0.0982 - acc: 0.9674 - val_loss: 0.1414 - val_acc: 0.9548
Epoch 160/200
10/10 [==============================] - 4s 377ms/step - loss: 0.0946 - acc: 0.9689 - val_loss: 0.1400 - val_acc: 0.9547
Epoch 161/200
10/10 [==============================] - 4s 378ms/step - loss: 0.0920 - acc: 0.9699 - val_loss: 0.1389 - val_acc: 0.9561
Epoch 162/200
10/10 [==============================] - 4s 405ms/step - loss: 0.0915 - acc: 0.9702 - val_loss: 0.1383 - val_acc: 0.9555
Epoch 163/200
10/10 [==============================] - 4s 379ms/step - loss: 0.0911 - acc: 0.9703 - val_loss: 0.1393 - val_acc: 0.9555
Epoch 164/200
10/10 [==============================] - 4s 374ms/step - loss: 0.0961 - acc: 0.9682 - val_loss: 0.1400 - val_acc: 0.9553
Epoch 165/200
10/10 [==============================] - 4s 378ms/step - loss: 0.0936 - acc: 0.9691 - val_loss: 0.1404 - val_acc: 0.9552
Epoch 166/200
10/10 [==============================] - 4s 380ms/step - loss: 0.0907 - acc: 0.9702 - val_loss: 0.1383 - val_acc: 0.9561
Epoch 167/200
10/10 [==============================] - 4s 378ms/step - loss: 0.0891 - acc: 0.9711 - val_loss: 0.1377 - val_acc: 0.9558
Epoch 168/200
10/10 [==============================] - 4s 407ms/step - loss: 0.0878 - acc: 0.9715 - val_loss: 0.1375 - val_acc: 0.9564
Epoch 169/200
10/10 [==============================] - 4s 380ms/step - loss: 0.0874 - acc: 0.9718 - val_loss: 0.1379 - val_acc: 0.9564
Epoch 170/200
10/10 [==============================] - 4s 377ms/step - loss: 0.0877 - acc: 0.9716 - val_loss: 0.1398 - val_acc: 0.9555
Epoch 171/200
10/10 [==============================] - 4s 379ms/step - loss: 0.0868 - acc: 0.9719 - val_loss: 0.1398 - val_acc: 0.9555
Epoch 172/200
10/10 [==============================] - 4s 376ms/step - loss: 0.0875 - acc: 0.9715 - val_loss: 0.1379 - val_acc: 0.9564
Epoch 173/200
10/10 [==============================] - 4s 379ms/step - loss: 0.0882 - acc: 0.9713 - val_loss: 0.1393 - val_acc: 0.9561
Epoch 174/200
10/10 [==============================] - 4s 379ms/step - loss: 0.0875 - acc: 0.9715 - val_loss: 0.1384 - val_acc: 0.9560
Epoch 175/200
10/10 [==============================] - 4s 378ms/step - loss: 0.0878 - acc: 0.9715 - val_loss: 0.1386 - val_acc: 0.9562
Epoch 176/200
10/10 [==============================] - 4s 409ms/step - loss: 0.0866 - acc: 0.9718 - val_loss: 0.1382 - val_acc: 0.9561
Epoch 177/200
10/10 [==============================] - 4s 410ms/step - loss: 0.0843 - acc: 0.9728 - val_loss: 0.1377 - val_acc: 0.9565
Epoch 178/200
10/10 [==============================] - 4s 380ms/step - loss: 0.0837 - acc: 0.9731 - val_loss: 0.1381 - val_acc: 0.9566
Epoch 179/200
10/10 [==============================] - 4s 380ms/step - loss: 0.0831 - acc: 0.9732 - val_loss: 0.1390 - val_acc: 0.9560
Epoch 180/200
10/10 [==============================] - 4s 380ms/step - loss: 0.0837 - acc: 0.9729 - val_loss: 0.1387 - val_acc: 0.9563
Epoch 181/200
10/10 [==============================] - 4s 378ms/step - loss: 0.0838 - acc: 0.9729 - val_loss: 0.1370 - val_acc: 0.9571
Epoch 182/200
10/10 [==============================] - 4s 378ms/step - loss: 0.0829 - acc: 0.9732 - val_loss: 0.1384 - val_acc: 0.9565
Epoch 183/200
10/10 [==============================] - 4s 380ms/step - loss: 0.0831 - acc: 0.9731 - val_loss: 0.1379 - val_acc: 0.9564
Epoch 184/200
10/10 [==============================] - 4s 382ms/step - loss: 0.0814 - acc: 0.9738 - val_loss: 0.1392 - val_acc: 0.9565
Epoch 185/200
10/10 [==============================] - 4s 381ms/step - loss: 0.0817 - acc: 0.9737 - val_loss: 0.1396 - val_acc: 0.9565
Epoch 186/200
10/10 [==============================] - 4s 380ms/step - loss: 0.0822 - acc: 0.9734 - val_loss: 0.1385 - val_acc: 0.9566
Epoch 187/200
10/10 [==============================] - 4s 378ms/step - loss: 0.0822 - acc: 0.9732 - val_loss: 0.1386 - val_acc: 0.9564
Epoch 188/200
10/10 [==============================] - 4s 377ms/step - loss: 0.0819 - acc: 0.9734 - val_loss: 0.1383 - val_acc: 0.9569
Epoch 189/200
10/10 [==============================] - 4s 380ms/step - loss: 0.0833 - acc: 0.9728 - val_loss: 0.1404 - val_acc: 0.9557
Epoch 190/200
10/10 [==============================] - 4s 378ms/step - loss: 0.0817 - acc: 0.9735 - val_loss: 0.1394 - val_acc: 0.9565
Epoch 191/200
10/10 [==============================] - 4s 379ms/step - loss: 0.0830 - acc: 0.9729 - val_loss: 0.1384 - val_acc: 0.9567
Epoch 192/200
10/10 [==============================] - 4s 379ms/step - loss: 0.0801 - acc: 0.9741 - val_loss: 0.1378 - val_acc: 0.9568
Epoch 193/200
10/10 [==============================] - 4s 409ms/step - loss: 0.0794 - acc: 0.9743 - val_loss: 0.1385 - val_acc: 0.9568
Epoch 194/200
10/10 [==============================] - 4s 379ms/step - loss: 0.0805 - acc: 0.9739 - val_loss: 0.1409 - val_acc: 0.9552
Epoch 195/200
10/10 [==============================] - 4s 377ms/step - loss: 0.0835 - acc: 0.9725 - val_loss: 0.1394 - val_acc: 0.9568
Epoch 196/200
10/10 [==============================] - 4s 406ms/step - loss: 0.0807 - acc: 0.9737 - val_loss: 0.1397 - val_acc: 0.9566
Epoch 197/200
10/10 [==============================] - 4s 381ms/step - loss: 0.0788 - acc: 0.9745 - val_loss: 0.1370 - val_acc: 0.9574
Epoch 198/200
10/10 [==============================] - 4s 409ms/step - loss: 0.0772 - acc: 0.9753 - val_loss: 0.1367 - val_acc: 0.9575
Epoch 199/200
10/10 [==============================] - 4s 382ms/step - loss: 0.0761 - acc: 0.9758 - val_loss: 0.1403 - val_acc: 0.9560
Epoch 200/200
10/10 [==============================] - 4s 406ms/step - loss: 0.0788 - acc: 0.9744 - val_loss: 0.1403 - val_acc: 0.9565
"""
# train: loss, accuracy, val: loss, accuracy
data = [txt[56:].replace("-", " ").split()[1::2] for txt in text.split("\n")[::2]]
accuracy = [[], []]
loss = [[], []]
for prog in data[1:]:
    print(prog)
    tl, ta, vl, va = prog
    accuracy[0].append(float(ta))
    accuracy[1].append(float(va))
    loss[0].append(float(tl))
    loss[1].append(float(vl))
plt.subplot(1, 2, 1)
plt.plot(accuracy[0], color = "orange", label = "train")
plt.plot(accuracy[1], color = "blue", label = "validation")
plt.legend()
plt.xlabel("epoch")
plt.ylabel("accuracy")
plt.subplot(1, 2, 2)
plt.plot(loss[0], color = "orange", label = "train")
plt.plot(loss[1], color = "blue", label = "validation")
plt.legend()
plt.xlabel("epoch")
plt.ylabel("loss")
plt.show()