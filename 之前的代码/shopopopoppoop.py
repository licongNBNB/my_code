# %%
import os
import time

a = 0
while (1):
    time2 = 0
    for i in range(0, 240):
        time.sleep(1)
        time2 = time2 + 1
        print(f'这是第{time2}秒')
        print(f"已刷新{a}次，恭喜")
    os.system(r"start /min C:\Users\聪\Desktop\改\buff_onsell.exe")
    time.sleep(240)
    os.system(r"taskkill /f /t /im buff_onsell.exe")
    a = a + 1


