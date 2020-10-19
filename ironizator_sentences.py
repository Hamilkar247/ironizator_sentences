# -*- coding: utf-8 -*-
import logging
import argparse
import sys
import pyperclip as pc


def def_params():
    parser = argparse.ArgumentParser(
            description='Script to Ironizing sentence'
    )
    #action="store_true" sprawia że potem już nie nie musze podawać liczby/stringa do tego argume    ntu
    parser.add_argument("-l", "--loghami", action='store_true', help="set debug")
    parser.add_argument("-s", "--sentence", help="sentence to ironizing", required=True)
    parser.add_argument("-p", "--pyperclip", action='store_true', help="output will be saved in clipboard")
    parser.add_argument("-u", "--underscores", action='store_true', help="change space to underscores for symbol link")
    args = parser.parse_args()
    if args.loghami:
        logging.basicConfig(level=logging.DEBUG)
        print("args:" + str(args))
    if args.underscores:
        logging.debug('dziendobry wlaczony underscores')
        logging.debug('args.underscores:'+str(args.underscores))
    return args


def concatenate_list_data(list, underscores):
    result= ''
    for element in list:
        if element=='_' and underscores==True:
            result += " "
            logging.debug("Hej jestem tutaj! underscors!")
        else:
            result += str(element)
    return result


def ironizator_sentences_def(sentence, underscores):
    logging.debug('Only shown in debug mode')
    logging.debug("input sentence:"+ sentence)

    i=1
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
    return concatenate_list_data(output_sentence, underscores)


def main():
    args=def_params()
    logging.debug('Only shown in debug mode')
    logging.debug("under:" + str(args.underscores))
    sentence=args.sentence
    sentence=ironizator_sentences_def(sentence, args.underscores)
    logging.debug("output sentence:"+ sentence)
    if args.pyperclip:
        pc.copy(sentence)
    print(sentence)


if __name__ == "__main__":
    main()
