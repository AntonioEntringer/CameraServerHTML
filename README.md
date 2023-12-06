### CameraServerHTML
Metodo simples para acesso das cameras do laboratório - LabSea

**Docker**
### Os códigos para composição do Docker estão no diretório "SourceFiles". Para executar o Docker, utilize o seguinte comando:

```bash
- docker run -d --network host camerasserver:latest
```

# Após a execução, os links para acessar as câmeras serão:

Camera 1: <ip_da_maquina_host>:5001
Camera 2: <ip_da_maquina_host>:5002
Camera 3: <ip_da_maquina_host>:5003
Camera 4: <ip_da_maquina_host>:5004

**Kubernetes**
### Para utilizar no Kubernetes, use os seguintes lançadores disponíveis no diretório "k8s":

- cameraserverdeploy.yaml
- cameraserver.yaml

# Aplique esses arquivos usando o comando:

```bash
kubectl apply -f cameraserverdeploy.yaml -f cameraserver.yaml
```

# Os links para acessar as câmeras no Kubernetes serão:

Camera 1: <ip_da_maquina_host>:31001
Camera 2: <ip_da_maquina_host>:31002
Camera 3: <ip_da_maquina_host>:31003
Camera 4: <ip_da_maquina_host>:31004

**Contato**
*Para mais informações, entre em contato através do e-mail: marcosmutzcontato@gmail.com*
