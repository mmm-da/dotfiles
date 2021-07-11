#!/usr/bin/python

import re
from subprocess import Popen, PIPE

p = Popen(['amixer', 'sget', 'Master'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
amixer_stdout, amixer_stderr = p.communicate()

if amixer_stdout:
    amixer_stdout = amixer_stdout.decode('utf-8')

if amixer_stderr: 
    raise Exception(str(amixer_stderr))

regex_result = re.search(r'\[(.*%)\] \[.*\] \[(on|off|.*)\]',amixer_stdout)

icon = ''
volume = ''

if not regex_result:
    icon = '⚠️'
    volume = '???'
else:
    volume = regex_result.group(1)
    numeric_volume = int(volume[:-1])
    if numeric_volume <= 5:
        icon = '🔈'     
    elif 5 < numeric_volume <= 40:
        icon = '🔉'
    else:
        icon = '🔊'

    if regex_result.group(2) == 'off':
        icon = '🔇'

print(f'{icon}{volume}')
