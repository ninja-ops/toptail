#!/usr/bin/env python
import sys, argparse, datetime, time, fileinput, operator

parser = argparse.ArgumentParser(prog='toptail')
parser.add_argument('-f', '--file', default='-', help='Filename, default - for STDIN')
parser.add_argument('-l', '--limit', type=int, default=10, help='Limit Output to n Values, default 0')
parser.add_argument('-c', '--column', type=int, default=7, help='Column of Item used to Group Counts, default 7')
parser.add_argument('-i', '--intervall', type=int, default=10, help='Refresh Intervall in Seconds, default 10')
parser.add_argument('-m', '--min', type=int, default=0, help='Minimal Count of Occurence to display the Value, default 0')
parser.add_argument('-s', '--seperator', type=int, default=32, help='Number of Char to split Value into Columns, default 32 for SPACE')
parser.add_argument('--version', action='version', version='%(prog)s 0.4.0')
args = parser.parse_args()

column=args.column
intervall=args.intervall
min=args.min
seperator=args.seperator
file=args.file
limit=args.limit

oldtime=int(time.time())
index = {}
for line in fileinput.input(file):
    newtime=int(time.time())
    chunks = line.strip().split(chr(seperator))
    try:
        key = chunks[column]
        try:
            index[key] = index[key] + 1;
        except KeyError:
            index[key] = 1
    except IndexError:
        True
    if (line.strip() == 'exit'):
      sys.exit()
    if (newtime-oldtime >= intervall):
        print(datetime.datetime.now())
        total=0
        sindex = sorted(index.items(), key=operator.itemgetter(1))
        if (limit == 0):
            for k in sindex:
                total = total + k[1]
                if k[1] > min:
                    print(k[1], '\t', '%.2f' % (k[1] / (newtime - oldtime)), '\t\t', k[0])
        else:
            for k in sindex:
                total = total + k[1]
            for p in range(0, limit):
                v=limit - p
                v=-v
                try:
                    k=sindex[v]
                    print(k[1], '\t', '%.2f' % (k[1] / (newtime - oldtime)), '\t\t', k[0])
                except IndexError:
                    True
        index = {}
        print('--------------------------------------------')
        print(total, '\t', '%.2f' % (total / (newtime - oldtime)), '\t', '*')
        oldtime = newtime
        print('--------------------------------------------')
