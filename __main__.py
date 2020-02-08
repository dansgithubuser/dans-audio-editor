import os
import sys

DIR = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(DIR, 'py-rpc-host'))

import rpc_host
import dans_audio_editor

rpc_host.serve(dans_audio_editor)
