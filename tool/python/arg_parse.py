#!/usr/bin/env python3
# https://stackoverflow.com/questions/7625786/type-dict-in-argparse-add-argument
import argparse
import yaml

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-fna', '--filename-arguments', type=yaml.load, default=None, required=True)
    args = parser.parse_args()
    print(args)

    # data = "{location: warehouse A, site: Gloucester Business Village}"
    # ans = parser.parse_args(['-fna', data])
    # print(ans.filename_arguments['site'])

if __name__ == '__main__':
    main()

