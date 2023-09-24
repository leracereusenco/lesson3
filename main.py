#array = [] #lista in care se pot stoca mai multe tipuri de valori
#se stocheaza mai multe valori intr-o singura variabila
# in c++ - tablou

#var = 10
#array = ["Math", "Info", "Physics", "General Culture"]
#Math - locul 1 - indexul 0
#Info - locul 2 - indexul 1
#array.append("English") #se mai adauga un element suplimentar
#array = sorted(array)  #doar in tipuri de date la fel
#array.sort()
#print(array)


#array = [1, 2, 3, 4, 5, 6]
#array = sorted(array)
#array.sort() #se sorteaza lista
#array.sort(reverse=True) #se reverseaza lista #=array.reverse()

#print(array) #se afiseaza lista
#print(sorted(array)) #se afiseaza lista sortata


#propunrerea propiei liste
#list = []
#list_lenght = int(input("Enter List Lenght\n"))

#for i in range(0, list_lenght):
   # element = int(input("Enter an Element\n"))
    #list.append(element)
#else:
    #print(list)
    #list.sort()
    #print(list)
    #list.sort(reverse=True)
    #print(list)


#verificarea prezentei valorii in lista
#list = [1,3,12,23,34,45,56,67,78,89,90,100]
#print(list[3]) #afisarea valorii cu indexul dat (23)
#if 12 in list:
    #print('True')
#else:
    #print('False')


#valoarea se printeaza dupa nr de index
#list = [1,3,12,23,34,45,56,67,78,89,90,100]
#print(list)
#for i in range(0, len(list)): #len(list) - lungimea listei, nr de valori
    #print(list[i])

#for e in list:
    #print(e)


#tuplu
#tuple = ("A", "B", "C", "D") #lista
#print(tuple[0])
#print(tuple + ("E", "Finish"))

#int_array = [1,2,3,1,5,2,6,7]
#int_array = set(int_array) #tip de colectie, care salveaza doar valori unice, fara duplicaturi
#set_array = {1,1,2,3,1,5,2,6,7}
#print(set_array)
#print(int_array)


#dictionare - colectie cu cheie si valoare
dex = {"Cod": "Python", "Extend": ".py", "Lesson": "3"} #{"Key": "Valoare"}
print(dex.get("Cod")) #se afiseaza nu dupa index, ci dupa cheie
print(dex) #se afiseaza dictionarul integral

dex.update({"Lesson": "4"}) #se schimba valoarea cheii "Lesson"
print(dex) #se afiseaza dictionarul cu cheia schimabata

for i in dex: #se afiseaza cheile si valorile din dictionar
    print(i)
    print(dex.get(i))


##T/a: diferenta intre tuplu si lista(array)
