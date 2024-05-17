thislist = ["apple", "orange", "banana", "cherry"]
print(thislist)
print(thislist[-2]) # [] 0dan saymaya başlar.

print(len(thislist))
print(type(thislist))

print(thislist[1:3]) #son sayı alınmaz - 1 2 alınır. [:n] - en baştan n'e kadar alır. [n:] - n'den başlar sona kadar alır.

search = "apple"
if search in thislist:
  print("Yes, 'apple' is in the fruits list")

thislist[1] = "blackcurrant"
print(thislist[1])
print(thislist)

thislist.insert(1, "watermelon") # instert araya eklemek için kullanılır, index numarasından fazla girilirse en sona ekler.
print(thislist)

thislist.append("peach") # index numarasına gerek kalmadan sona ekler.
print(thislist)

# list.extend(başka list) iki listeyi birleştirir.
# list.remove("eleman") elemanı kaldırmak için.
# list.pop(n) n. elemanı kaldırır. (0) olursa son elemanı kaldırır.
# del list[n] - n. elemanı kaldırır.
# del list - listeyi siler.
# list.clear() - listenin içindekileri silinir.
# for x in thislist: print(x) içindekileri kontrol eder
del thislist[0]
print(thislist)

for x in thislist:
    print(x)

for i in range(2):
    print(thislist[i])

