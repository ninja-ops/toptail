# toptail

## Why ?

Sometimes you need the count of groups of items within logfiles, similar to SQL "count(*) as Hits where Hits > 42 group by ColumnName order by Hits desc limit 0, 23".

Sometimes you need this ASAP, because you need quick insights of whats going.

Sometimes your boilerplates for awk/sed/cat/grep/sort/uniq are "buggy/quirky" and doesnt fit right now.

Sometimes you need this in Real-Time as a continous loop every x seconds.

## Installation

### Linux

```shell
git clone https://github.com/ninja-ops/toptail
sudo chmod +x toptail/src/toptail.py
sudo ln -s "$(pwd)/toptail/src/toptail.py" /usr/bin/toptail
```

### Windows

  * Download Master.Zip
  * Get Python for Windows https://www.python.org/downloads/windows/
  * "melt" "everything" "together" ..

## General Usage

You need to feed toptail with data either via STDIN or as named file. It is recommend to use additional Tools like 'tail' in conjunction with '-f'.

You define a Column splitted by Char used for grouping.

Column is a number, beginning with 0 as start. Default is 7, as this is the username in IIS Logs.

Splitting is done by defining a Seperator as Char/Number, e.g. 32 for SPACE. Default is 32/SPACE.

If you define a Limit of Items to be shown, the highest n counts will be displayed.

You can set a minimum Count of occurence for the list. Sometimes it makes sense to exclude all Items below 5 or 2.

```shell
usage: toptail [-h] [-f FILE] [-l LIMIT] [-c COLUMN] [-i INTERVALL] [-m MIN]
               [-s SEPERATOR] [--version]

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Filename, default - for STDIN
  -l LIMIT, --limit LIMIT
                        Limit Output to n Values, default 0
  -c COLUMN, --column COLUMN
                        Column of Item used to Group Counts, default 7
  -i INTERVALL, --intervall INTERVALL
                        Refresh Intervall in Seconds, default 10
  -m MIN, --min MIN     Minimal Count of Occurence to display the Value,
                        default 0
  -s SEPERATOR, --seperator SEPERATOR
                        Number of Char to split Value into Columns, default 32
                        for SPACE
  --version             show program's version number and exit
```
## History

Toptail was developed under "pressure". So excuse any "quirks". But works for me.

Toptail is inspired by the following tools ..

  * top
  * apachetop
  * uniq
  * count
  * cut
