# === DZ 40 Генераторы ===
def all_variants(text):
 for i in range(len(text)):
     for t in range(len(text) - i):
         yield text[t:t + i + 1]


# я вообще забыл, что у нас есть срезы. хах. пришлось воспользоваться гуглом. там уже кто-то даже искал такой вопрос,
# но я еще сам разобрался, освежил память так сказать)

a = all_variants("abc")
for i in a:
    print(i)

