import logging
import argparse
import sys


def def_params():
    parser = argparse.ArgumentParser(
            description='Script to Ironizing sentence'
    )
    #action="store_true" sprawia że potem już nie nie musze podawać liczby/stringa do tego argume    ntu
    parser.add_argument("-l", "--loghami", action='store_true', help="set debug")
    parser.add_argument("-s", "--sentence", help="sentence to ironizing", required=True)
    args = parser.parse_args()
    if args.loghami: 
        logging.basicConfig(level=logging.DEBUG)
    return args        


def concatenate_list_data(list):
    result= ''
    for element in list: 
        result += str(element)
    return result


def ironizator_sentences_def(sentence):
    logging.debug('Only shown in debug mode')
    logging.debug("input sentence:"+ sentence)
    i=0
    output_sentence=[]
    for char in sentence:
        if i==0:
            logging.debug(char.upper())
            i=i+1
            output_sentence.append(char.upper())
        else:
            logging.debug(char.lower())
            i=i-1
            output_sentence.append(char.lower())
    return concatenate_list_data(output_sentence)


def main():
    args=def_params()
    logging.debug('Only shown in debug mode')
    sentence=args.sentence
    sentence=ironizator_sentences_def(sentence)
    logging.debug("output sentence:"+ sentence)
    print(sentence)


if __name__ == "__main__":
    main()
