from ht10_proj.quotes.templatetags.models2 import Authors, Quotes
import connect2 as connect2
import os

while True:
    num = 0
    c = 0
    flag = 0
    
    print()
    print('Введіть запит:')
    print("- за ім'ям (Albert, Martin) - введіть ім'я та натисніть Enter")
    print('- за тегом (change, deep-thoughts, thinking, world, humor, obvious, simile) - введіть тег та натисніть Enter')
    print('- за кількома тегами через кому без пробілів - уведіть теги та натисніть Enter')
    print('вийти з режиму запитів - Enter')
    print('')
    a = input()
    if a == '':
        os(quit())
    if a == 'Albert' or a == 'Martin':
        nnijs = Authors.objects()
               
        for nnij_ in nnijs:   
            if a in nnij_.fullname:
                flag = 1
                zap = [f'знайдено автора: {nnij_.fullname}, народився: {nnij_.born_date}, {nnij_.born_location}, про автора: {nnij_.description}']
                print(zap)
                print()
                continue
    if a == 'change' or a == 'deep-thoughts' or a == 'thinking' or a == 'world' or a == 'humor' or a == 'obvious' or a == 'simile':
        tags_ = Quotes.objects()
        for tag_ in tags_:
            if a in tag_.tags:
                flag = 1
                zap = [f'знайдено цитату: {tag_.quote}']
                print(zap)
                print()
                continue       
    
    b = a.split(",")
    num = len(b)
       
    if num == 1 and flag == 0:
        print('УВАГА! Запит неточний, повторіть його!')
        print()
        continue
        
    if num > 1:
        tags_ = Quotes.objects()
        for tag_ in tags_:
            for b1 in b:
                if b1 in tag_.tags:
                    text = tag_.quote                    
                    print([f'знайдено цитату: {text}'])  
                    c = +1
                if c == 0:
                    print('УВАГА! Запит неточний, повторіть його!')
                    print()
                    c = 0
                    continue
        continue     
                    

