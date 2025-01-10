# === DZ 40 Генераторы ===
def all_variants(text):
 for i in range(len(text)):
     for t in range(len(text) - i):
         yield text[t:t + i + 1]


a = all_variants("abc")
for i in a:
    print(i)

