# Use uma imagem base do Python
FROM python:3.8-slim

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia os arquivos necessários para o diretório de trabalho
COPY httpsubscribe.py .
COPY start_servers.sh .
COPY templates templates

# Instala as dependências necessárias
RUN apt-get update && \
    apt-get install -y libgl1-mesa-glx libglib2.0-0 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Instala as dependências necessárias
RUN pip install --upgrade pip
RUN pip install flask
RUN pip install is-wire
RUN pip install opencv-python
RUN pip install amqp==2.4.2 
RUN pip install cachetools==4.2.4
RUN pip install certifi==2023.5.7
RUN pip install charset-normalizer==3.1.0
RUN pip install colorlog==3.1.4
RUN pip install enum34==1.1.6
RUN pip install google-api-core==1.19.1
RUN pip install google-auth==1.35.0
RUN pip install googleapis-common-protos
RUN pip install idna==3.4 is-msgs==1.1.10
RUN pip install is-wire==1.2.0 numpy==1.24.3
RUN pip install opencensus==0.5.0
RUN pip install opencensus-context==0.1.0
RUN pip install prometheus-client==0.3.1
RUN pip install protobuf==3.20.0
RUN pip install pyasn1==0.5.0
RUN pip install pyasn1-modules==0.3.0
RUN pip install pytz==2023.3
RUN pip install requests==2.30.0
RUN pip install rsa==4.9
RUN pip install six==1.16.0
RUN pip install urllib3==2.0.2 
RUN pip install vine==1.3.0

# Torna o script de inicialização executável
RUN chmod +x start_servers.sh
#RUN ./start_servers.sh

# Expõe a porta 5000 (ou outra porta de sua escolha)
#EXPOSE 5000

# Inicia os servidores ao iniciar o contêiner
CMD ["./start_servers.sh"]
