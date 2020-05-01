# This code is shown in https://pypi.org/project/v4l2/

import v4l2ForPython3 as v4l2
import fcntl

vd = open('/dev/video0', 'w')
cp = v4l2.v4l2_capability()
print(fcntl.ioctl(vd, v4l2.VIDIOC_QUERYCAP, cp))
print(cp.driver)
print(cp.card)
