#!/usr/bin/env python

import sys
import json
import time
from random import randint
from utils import get_task_dict, save_output_json

task_dict = get_task_dict(sys.argv[1])

task_start = int(time.time())

# do the real work here
time.sleep(randint(1,10))


# complete the task

task_stop = int(time.time())

output_json = {
    'xml_file': '/path/to/xml_file.xml',
    'xml_file_name': 'xml_file.xml',
    'xml_file_size': 23233,
    'xml_file_md5sum': 'xxxxxxxx',
    'runtime': {
        'task_start': task_start,
        'task_stop': task_stop
    }
}

save_output_json(output_json)

