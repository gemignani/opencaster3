#!/usr/bin/env python
import os
from dvbobjects.PSI.PAT import *
from dvbobjects.PSI.NIT import *
from dvbobjects.PSI.SDT import *
from dvbobjects.PSI.PMT import *
from dvbobjects.SBTVD.Descriptors import *
tvd_ts_id = 0x073b # ID de red.
tvd_orig_network_id = 0x073b # ID de red original.
ts_freq = 533 # Frecuencia de transmisión
ts_remote_control_key = 0x05 # Tecla de control remoto.
tvd_service_id_sd = 0xe760 # ID de servicio de TV Digital.
tvd_pmt_pid_sd = 1031 # PID de la PMT del servicio.
