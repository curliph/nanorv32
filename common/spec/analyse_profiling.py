#!/usr/bin/env python

import argparse
import re
import sys
import pprint as pp
import pickle
from operator import itemgetter

def get_args():
    """
    Get command line arguments
    """
    parser = argparse.ArgumentParser(description="""
Analyse results provided by the --profile option of the Nanorv32 simulator
                   """)
    parser.add_argument('--profile', action='store', dest='profile',
                        help='Profiling data from the simulator (Pickle format)', default="")
    return parser.parse_args()

if __name__ == '__main__':

    args = get_args()

    if args.profile != "":
        with open(args.profile) as f:
            profile_info = pickle.load(f)
            pp.pprint(profile_info)
            pairs = [(x,profile_info[x]['__count__']) for x in profile_info.keys()]
            #pp.pprint(pairs)
            sorted_pairs = sorted(pairs, key=itemgetter(1))
            pp.pprint(sorted_pairs)
            cycle = 0
            for f,c in sorted_pairs:
                cycle += c
        print "-I Done - Cycles : {}".format(cycle)
