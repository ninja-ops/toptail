# toptail

## Why ?

Sometimes you need the count of groups of items within logfiles, similar to SQL "count(*) as Hits group by ColumnName".

Sometimes you need this in Real-Time as a continous loop every x seconds.

Sometimes you need this ASAP, because you need quick insights of whats going.

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
