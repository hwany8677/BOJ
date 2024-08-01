sleep=int(input())
awake=int(input())
sleep=sleep-24 if sleep>=20 and sleep<=23 else sleep
print(awake-sleep)