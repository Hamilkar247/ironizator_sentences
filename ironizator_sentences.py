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


def main():
    args=def_params()
    logging.debug('Only shown in debug mode')
    logging.debug("input sentence:"+ args.sentence)
    sentence_for_irony=args.sentence
    i=0
    for char in sentence_for_irony:
        if i==0:
            logging.debug(char.upper())
            i=i+1
        else:
            logging.debug(char)
            i=i-1


if __name__ == "__main__":
    main()
