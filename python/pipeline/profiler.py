#   Copyright (c) 2020 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# pylint: disable=doc-string-missing

<<<<<<< HEAD
=======
import os
import sys
if sys.version_info.major == 2:
    import Queue
elif sys.version_info.major == 3:
    import queue as Queue
else:
    raise Exception("Error Python version")
import time

>>>>>>> d84910a1180061b57c51824e35e3ca5c857eb3b5

class TimeProfiler(object):
    def __init__(self):
        self._pid = os.getpid()
        self._print_head = 'PROFILE\tpid:{}\t'.format(self._pid)
        self._time_record = Queue.Queue()
        self._enable = False

    def enable(self, enable):
        self._enable = enable

    def record(self, name_with_tag):
        if self._enable is False:
            return
        name_with_tag = name_with_tag.split("_")
        tag = name_with_tag[-1]
        name = '_'.join(name_with_tag[:-1])
        self._time_record.put((name, tag, int(round(time.time() * 1000000))))

    def print_profile(self):
        if self._enable is False:
            return
<<<<<<< HEAD
        print_str = self._print_head
=======
        sys.stderr.write(self._print_head)
>>>>>>> d84910a1180061b57c51824e35e3ca5c857eb3b5
        tmp = {}
        while not self._time_record.empty():
            name, tag, timestamp = self._time_record.get()
            if name in tmp:
                ptag, ptimestamp = tmp.pop(name)
<<<<<<< HEAD
                print_str += "{}_{}:{} ".format(name, ptag, ptimestamp)
                print_str += "{}_{}:{} ".format(name, tag, timestamp)
            else:
                tmp[name] = (tag, timestamp)
        print_str += "\n"
        sys.stderr.write(print_str)
=======
                sys.stderr.write("{}_{}:{} ".format(name, ptag, ptimestamp))
                sys.stderr.write("{}_{}:{} ".format(name, tag, timestamp))
            else:
                tmp[name] = (tag, timestamp)
        sys.stderr.write('\n')
>>>>>>> d84910a1180061b57c51824e35e3ca5c857eb3b5
        for name, item in tmp.items():
            tag, timestamp = item
            self._time_record.put((name, tag, timestamp))
