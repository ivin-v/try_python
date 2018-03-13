

#import string
import re
import random
import time



import ref       # массив местоимений ref.py
import psych     # массив фраз



#----Обработка зеркалки местоимения в 2-е лицо (ref.py)  --------

def reflect(fragment):
    tokens = fragment.lower().split()
    for i, token in enumerate(tokens):
        if token in ref.reflections:
            tokens[i] = ref.reflections[token]
    return ' '.join(tokens)

#----Обработка совпадений слов в фразе (файл psych.py) --------

def analyze(statement):
    for pattern, responses in psych.psychobabble:
        match = re.match(pattern, statement.rstrip(".!"))
        if match:
            response = random.choice(responses)
            return response.format(*[reflect(g) for g in match.groups()])


#----Ввод/вывод--------

def main():
#    print(time.ctime())           # выводим текущую дату и время
#    print (psych.psychobabble)

    while True:
        statement = input("> ")
        
        print (analyze(statement))

#        psych.psychobabble.append(statement) #добавление в список

#так ка надо не рабаботает. должен быть ввод отсутствующих вопросов-ответов и корректировка        
        if statement == "исправить":
           old_statement = (input("что исправить> "))
           new_statement = (input("на что исправить> "))
           for i in range(len(psych.psychobabble)):        #листаем список
               if psych.psychobabble[i] == old_statement:  #ищим совпадение
                  print (psych.psychobabble[i])
                  psych.psychobabble[i] = new_statement    #заменяем слово
   #               del psych.psychobabble[-2]                       #удаляем слово "исправить"
    
   

           
        
#        print (psych.psychobabble)

            
        if statement == "q":
            break
        
        
        
            
if __name__ == "__main__":
    main()
