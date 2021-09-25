from datetime import datetime
def tegs():
         current_datetime = datetime.now()
         mas = []
         f = open("теги.txt",'r',encoding='utf-8')
         while True:
                  tmas = f.readline().split()
                  if tmas==[]:
                           break
                  else:
                           mas.append(tmas)
         f.close()                  
         return mas[current_datetime.day]
