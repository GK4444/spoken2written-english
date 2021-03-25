from rules import rules
import re
from itertools import islice


def convert():
    output_para=''
    para = input("\nEnter Your paragraph of spoken english:\n")
    if not para:
        raise ValueError("NO INPUT!!!")

    words_of_para =para.split()
    no_of_words = len(words_of_para)

    numbers = rules['Numbers']
    abbreviations = rules['Abbreviations']
    repetitions = rules['Repetitions']
    currencies = rules['Currencies']

    lit = iter(enumerate(words_of_para))
    for idx, word in lit:
        if word.lower() in currencies:
            output_para = output_para +" "+str(currencies[word]) + str(numbers[words_of_para[idx-1].lower()])
        
        elif (idx+2) < no_of_words and word+" "+words_of_para[idx+1] in abbreviations:
            output_para = output_para +" "+ str(abbreviations[word+" "+words_of_para[idx+1]])
            next(islice(lit, 1,1), None)

        elif word in repetitions:
            if words_of_para[idx+1][-1] == '.':
                output_para = output_para +" "+ str(words_of_para[idx+1][:-1]*repetitions[word])+"."
            else:
                output_para = output_para +" "+ str(words_of_para[idx+1]*repetitions[word])

            next(islice(lit, 1,1), None)

        elif word in numbers:
            if words_of_para[idx+1][:-1] not in currencies:
                output_para = output_para +" "+ str(numbers[word])
        
        else:
            output_para = output_para +" "+ words_of_para[idx]
    
    print(f"\nConverted Written English Paragraph:\n{output_para}")

if __name__ == '__main__':
    convert()