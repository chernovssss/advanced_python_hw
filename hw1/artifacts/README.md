```bash
(.venv)  chernov@DESKTOP-4QEAK3M ~\....\advanced_python_hw  master  python .\hw1\src\main.py -h              
usage: nl_main.py [-h] [-b {a,t}] [-n {ln,rn,rz}] [-w NUMBER_WIDTH] [file]

Python version of the nl command

positional arguments:
  file                  Input file to number. If not provided, uses standard input.

options:
  -h, --help            show this help message and exit
  -b {a,t}, --body-numbering {a,t}
                        Specify the type of line numbering to use.
  -n {ln,rn,rz}, --number-format {ln,rn,rz}
                        Specify the line numbering format to use.
  -w NUMBER_WIDTH, --number-width NUMBER_WIDTH
                        Use a number of columns for the line numbers.
```

```bash
(.venv)  chernov@DESKTOP-4QEAK3M ~\....\advanced_python_hw  master  python .\hw1\src\main.py .\hw1\artifacts\test_file.txt -b a 
     0 but you didnt have to cut me off
     1 make out like it never happened and that we were nothing
     2 and i dont even need your love
     3 but you treat me like a stranger and that feels so rough
     4 no you didnt have to stoop so low
     5 have your friends collect your records and then change your number
     6 i guess that i dont need that though
     7 now youre just somebody that i used to know
     8 now youre just somebody that i used to know
     9 now youre just somebody that i used to know
(.venv)  chernov@DESKTOP-4QEAK3M ~\....\advanced_python_hw  master  python .\hw1\src\main.py .\hw1\artifacts\test_file.txt -w 12 -b t -n ln
0            but you didnt have to cut me off
1            make out like it never happened and that we were nothing
2            and i dont even need your love
3            but you treat me like a stranger and that feels so rough
4            no you didnt have to stoop so low
5            have your friends collect your records and then change your number
6            i guess that i dont need that though
7
8
9            now youre just somebody that i used to know
10           now youre just somebody that i used to know
11           now youre just somebody that i used to know
12
13
14
15
(.venv)  chernov@DESKTOP-4QEAK3M ~\....\advanced_python_hw  master  python .\hw1\src\main.py .\hw1\artifacts\test_file.txt -w 12 -b t -n rz
000000000000 but you didnt have to cut me off
000000000001 make out like it never happened and that we were nothing
000000000002 and i dont even need your love
000000000003 but you treat me like a stranger and that feels so rough
000000000004 no you didnt have to stoop so low
000000000005 have your friends collect your records and then change your number
000000000006 i guess that i dont need that though
000000000007
000000000008
000000000009 now youre just somebody that i used to know
000000000010 now youre just somebody that i used to know
000000000011 now youre just somebody that i used to know
000000000012
000000000013
000000000014
000000000015
(.venv)  chernov@DESKTOP-4QEAK3M ~\....\advanced_python_hw  master  python .\hw1\src\main.py .\hw1\artifacts\test_file.txt -w 12 -b a -n rn
           0 but you didnt have to cut me off
           1 make out like it never happened and that we were nothing
           2 and i dont even need your love
           3 but you treat me like a stranger and that feels so rough
           4 no you didnt have to stoop so low
           5 have your friends collect your records and then change your number
           6 i guess that i dont need that though
           7 now youre just somebody that i used to know
           8 now youre just somebody that i used to know
           9 now youre just somebody that i used to know
(.venv)  chernov@DESKTOP-4QEAK3M ~\....\advanced_python_hw  master  python .\hw1\src\main.py -w 12 -b a -n rn
that 
           0 that 
i 
           1 i 
used 
           2 used 
to 
           3 to 
know 
           4 know 


end
           5 end
^C
```

```bash
(.venv)  chernov@DESKTOP-4QEAK3M ~\....\advanced_python_hw  master  python .\hw1\src\tail_main.py --help                                                          
usage: tail_main.py [-h] [-n LINES] [files ...]

Python version of the tail command

positional arguments:
  files                 The file to display the last lines of

options:
  -h, --help            show this help message and exit
  -n LINES, --lines LINES
                        Number of lines to display
```

```bash
(.venv)  chernov@DESKTOP-4QEAK3M ~\....\advanced_python_hw  master  python .\hw1\src\tail_main.py .\hw1\artifacts\test_file.txt .\hw1\artifacts\test_file.txt -n 5
==> .\hw1\artifacts\test_file.txt <==
now youre just somebody that i used to know





==> .\hw1\artifacts\test_file.txt <==
now youre just somebody that i used to know





(.venv)  chernov@DESKTOP-4QEAK3M ~\....\advanced_python_hw  master  python .\hw1\src\tail_main.py -n 2                                                            
1
2
3
4
3
4
^C
(.venv)  chernov@DESKTOP-4QEAK3M ~\....\advanced_python_hw  master  
```