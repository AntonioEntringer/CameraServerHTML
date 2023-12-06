#!/bin/bash

python3 httpsubscribe.py --camera 1 --port 5001 &
python3 httpsubscribe.py --camera 2 --port 5002 &
python3 httpsubscribe.py --camera 3 --port 5003 &
python3 httpsubscribe.py --camera 4 --port 5004 &

# Mantém o contêiner em execução
tail -f /dev/null
