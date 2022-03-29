import time;
reverseCount = 15
count = 1
print("%02d" % reverseCount)
if count % 1 == 0:
    print("\n\033[1mPlease wait a minute to display the rest of the files\033[0m")
    while reverseCount >= 0:
        print(f"\r⏰ \033[96m{'%02d' % reverseCount} seconds left\033[0m", end = '\r')
        time.sleep(0.5)
        reverseCount -= 1
    print()
