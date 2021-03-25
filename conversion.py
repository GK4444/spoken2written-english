from rules import rules
import re
from itertools import islice


def convert():
    output_para=''
    para = input("\nEnter Your paragraph of spoken english:\n")
    if not para:
        raise ValueError("NO INPUT!!!")

    # words_of_para = re.split('(?<!\d)[,.]|[,.](?!\d)', para)
    words_of_para =para.split()
    
    # para_split = para.split()
    # print(f'**RE**:{words_of_para}')
    # print(f'**PARA.SPLIT**:{words_of_para}')
    
    no_of_words = len(words_of_para)

    numbers = rules['Numbers']
    abbreviations = rules['Abbreviations']
    repetitions = rules['Repetitions']
    currencies = rules['Currencies']
    # print(rules)
    lit = iter(enumerate(words_of_para))
    for idx, word in lit:
        last_word=False
        converted=False
        if word[-1] == '.':
            word=word[:-1]
            # last_word=True
        if word.lower() in currencies:
            # converted = True
            output_para = output_para +" "+str(currencies[word]) + str(numbers[words_of_para[idx-1].lower()])
        
        elif (idx+2) < no_of_words and word+" "+words_of_para[idx+1] in abbreviations:
            # print(f'**PRINTING**:{word+" "+words_of_para[idx+1]}')
            output_para = output_para +" "+ str(abbreviations[word+" "+words_of_para[idx+1]])
            # converted = True
            # idx+=2
            next(islice(lit, 1,1), None)

        elif word in repetitions:
            # print(words_of_para[idx+1])
            if words_of_para[idx+1][-1] == '.':
                # words_of_para[idx+1]=words_of_para[idx+1][:-1]
                output_para = output_para +" "+ str(words_of_para[idx+1][:-1]*repetitions[word])+"."
            else:
                output_para = output_para +" "+ str(words_of_para[idx+1]*repetitions[word])
                # print(f'output_para:{str(words_of_para[idx+1][:-1]*3)+"."}')
            
            # converted = True
            next(islice(lit, 1,1), None)

        elif word in numbers:
            if words_of_para[idx+1][:-1] not in currencies:
                output_para = output_para +" "+ str(numbers[word])
            # converted = True
        
        else:
            # if last_word and converted:
            #     print('!!!!!!!!!!!!')
            #     output_para += '.'
            # else:
            output_para = output_para +" "+ words_of_para[idx]
    
    print(f"\nConverted Written English Paragraph:\n{output_para}")
    print('*'*50)
    print(f'**PARA.SPLIT**:{words_of_para}')

if __name__ == '__main__':
    convert()