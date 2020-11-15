

import subprocess
import shlex


for x in range(0, 25):
    subprocess.call(shlex.split('./blueBox.sh box%d %d %d' % (x, -25, x*2 - 25)))

for x in range(0, 25):
    subprocess.call(shlex.split('./blueBox.sh box%d %d %d' % (x+25, x*2 - 25, 25)))

for x in range(0, 25):
    subprocess.call(shlex.split('./blueBox.sh box%d %d %d' % (x+50, 25, -x*2 + 25)))

for x in range(0, 25):
    subprocess.call(shlex.split('./blueBox.sh box%d %d %d' % (x+75, -x*2 + 25, -25)))
