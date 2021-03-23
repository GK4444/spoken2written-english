from word2number import w2n 
import rules

def check_front_last(word):
    front=""
    last=""
    if(len(word)>1):
        if word[-1]==',' or word[-1]=='.':
            last=word[-1]
            word=word[:-1]
        if word[0]==',' or word[0]=='.':
            front=word[0]
            word=word[1:]
    return front,word,last

class spoken2written:

    def __init__(self):
        self.rules=rules.rules
        self.input_para=""
        self.ouptut_para=""

    def get_user_input(self):

        self.paragraph=input("\nEnter Your paragraph of spoken english:\n")

        if not self.paragraph:
            raise ValueError("NO INPUT!!!")

    def show_output(self):
        print(f"\nConverted Written English Paragraph:\n{self.ouptut_para}")

    
    # main conversion function of spoken to written english 
    def Convert(self):
        # splitting paragraph into individual words
        words_of_para=self.paragraph.split()

        # accessing conversion rules
        numbers=self.rules['Numbers']
        abbreviations=self.rules['Abbreviations']
        repetitions=self.rules['Repetitions']
        currencies=self.rules['Currencies']
        i=0
        no_of_words=len(words_of_para)
        # loop thorugh all words in the paragraph 
        while i<no_of_words: 
            front,word,last=check_front_last(words_of_para[i])

            if i+1!= no_of_words:
                front_n,next_word,last_n=check_front_last(words_of_para[i+1])
                if word.lower() in numbers.keys() and (next_word.lower() in currencies):
                    self.ouptut_para=self.ouptut_para+" "+front+str(currencies[next_word.lower()])+str(numbers[word.lower()])+last
                    i=i+2

                elif word.lower() in repetitions.keys() and len(next_word)==1:
                    self.ouptut_para=self.ouptut_para+" "+front_n+(next_word*repetitions[word.lower()])+last_n
                    i=i+2
                elif (word+" "+next_word) in abbreviations.keys():
                    self.ouptut_para=self.ouptut_para+" "+front+word+next_word+last_n
                    i=i+2
                else:
                    self.ouptut_para=self.ouptut_para+" "+words_of_para[i]
                    i=i+1
            else:
                self.ouptut_para=self.ouptut_para+" "+words_of_para[i]
                i=i+1


if __name__ == '__main__':
    obj_spoken=spoken2written()

    obj_spoken.get_user_input()
    obj_spoken.Convert()
    obj_spoken.show_output()