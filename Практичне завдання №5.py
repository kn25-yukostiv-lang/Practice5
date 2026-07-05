MOD = 12345

n = int(input("Введіть довжину послідовності n: "))

dp0 = 1
dp1 = 0
dp2 = 0

for i in range(n):
    new0 = (dp0 + dp1 + dp2) % MOD
    new1 = dp0
    new2 = dp1

    dp0 = new0
    dp1 = new1
    dp2 = new2

result = (dp0 + dp1 + dp2) % MOD

print(f"Кількість шуканих послідовностей: {result}")