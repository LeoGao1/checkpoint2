#!/usr/bin/env python

import sys
import json




def main(targets):

    if 'test' in targets:
        with open('test/testdata/all_four-000000.db') as db:

            print('database loaded')

    return


if __name__ == '__main__':
    # run via:
    # python main.py data model
    targets = sys.argv[1:]
    main(targets)
