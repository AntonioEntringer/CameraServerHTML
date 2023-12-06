#!/bin/bash

# Lista de pacotes a serem instalados
pacotes=(
    "amqp==2.4.2"
    "cachetools==4.2.4"
    "certifi==2023.5.7"
    "charset-normalizer==3.1.0"
    "colorlog==3.1.4"
    "enum34==1.1.6"
    "google-api-core==1.19.1"
    "google-auth==1.35.0"
    "googleapis-common-protos==1.52.0"
    "idna==3.4"
    "is-msgs==1.1.10"
    "is-wire==1.2.0"
    "numpy==1.24.3"
    "opencensus==0.5.0"
    "opencensus-context==0.1.0"
    "opencv-python==4.7.0.72"
    "prometheus-client==0.3.1"
    "protobuf==3.20.0"
    "pyasn1==0.5.0"
    "pyasn1-modules==0.3.0"
    "pytz==2023.3"
    "requests==2.30.0"
    "rsa==4.9"
    "six==1.16.0"
    "urllib3==2.0.2"
    "vine==1.3.0"
)

# Itera sobre a lista de pacotes e os instala
for pacote in "${pacotes[@]}"; do
    pip3 install "$pacote"
done
