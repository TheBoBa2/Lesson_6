seconds = int(input("Введіть значення: "))

if not (0 <= seconds < 8640000):
    print("невірне значення")
    exit()

days, rem = divmod(seconds, 86400)
hours, rem = divmod(rem, 3600)
minutes, sec = divmod(rem, 60)

if 11 <= days % 100 <= 14:
    day_word = "днів"
elif days % 10 == 1:
    day_word = "день"
elif 2 <= days % 10 <= 4:
    day_word = "дні"
else:
    day_word = "днів"

print(f"{days} {day_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(sec).zfill(2)}")
