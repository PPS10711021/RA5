# 📦 Despliegue de Infraestructura con K3s y K9s – RA5.4

## 📌 Introducción

### 🔍 ¿Qué es Kubernetes?
Kubernetes (K8s) es una plataforma open-source para orquestar contenedores. Permite automatizar despliegues, escalar y gestionar aplicaciones en entornos distribuidos.

- ✅ Automatización del despliegue  
- ✅ Escalado dinámico de servicios  
- ✅ Gestión de redes y almacenamiento  
- ✅ Alta disponibilidad en entornos de producción

---

## 🧠 1. K3s: Kubernetes Ligero para entornos Edge

K3s es una distribución **ligera** de Kubernetes creada por Rancher Labs. Ideal para IoT, edge computing y entornos con pocos recursos.

- 🔹 Instalación con un solo binario (< 100 MB)  
- 🔹 Requiere menos memoria y CPU  
- 🔹 Compatible con kubectl y el ecosistema Kubernetes  
- 🔹 Modos de operación: **Single-Node** y **HA (Alta Disponibilidad)**

---

### 🏗️ 1.1 Arquitectura Single-Node

Todo el clúster en un solo nodo.  
Ideal para desarrollo y pruebas locales.

- 📦 Servicio desplegado: `nginx` con 2 réplicas  
- 📸 Capturas: nodo activo, pods corriendo

---

### 🛡️ 1.2 Arquitectura HA (High Availability)

Configuración de múltiples nodos **server** con base de datos externa o etcd embebido.  
Requiere mínimo 3 nodos en modo embedded para quorum.

- 📦 Servicio desplegado: `nginx` con 2 réplicas  
- 📸 Capturas: clúster en HA, servicios en ejecución

---

## 🔧 2. kubectl – Herramienta de gestión

- 🔹 Interfaz oficial en línea de comandos  
- 🔹 Se comunica con el API server  
- 🔹 Permite crear, aplicar y eliminar recursos del clúster  
- 🔹 Usa el archivo `~/.kube/config`

---

## 🖥️ 3. K9s – TUI para Kubernetes

Interfaz basada en terminal que permite navegar y observar los recursos del clúster en tiempo real.

- 🔹 Visualización de pods, servicios, logs  
- 🔹 Interacción rápida con recursos  
- 🔹 Ideal para administración diaria y validaciones

---

## 🎯 Objetivos de la práctica

**RA5** – Implantar sistemas seguros de desplegado de software usando herramientas de automatización.

- ✔ **CA5.A**: Instalación y configuración de clústeres con K3s  
- ✔ **CA5.B**: Validación funcional del clúster mediante kubectl y K9s  
- ✔ **CA5.C**: Despliegue de servicios y visualización del estado

---

## 🛠️ Actividades

### 🔧 5.1 – Despliegue en modo Single-Node

- ✅ Instalar K3s  
- ✅ Desplegar `nginx` con 2 réplicas  
- ✅ Instalar K9s y validar  
- 📸 Capturas: clúster, pods, servicio nginx, uso de K9s

Instalamos Kubernetes mediente un script oficial.

```bash
curl -sfL https://get.k3s.io | sh -
```

📸 Captura:

![instalar](https://github.com/PPS10711021/RA5/blob/main/RA5_4/assets/instalar.png)

Definimos el deployment:

```bash
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 2
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:stable
        ports:
        - containerPort: 80
```

Despliegue del deployment de nginx:

```bash
sudo kubectl apply -f nginx_deployment.yml
```

📸 Captura:

![nginx_deploy](https://github.com/PPS10711021/RA5/blob/main/RA5_4/assets/nginx_deploy.png)

Verificación de los pods:

```bash
sudo kubectl get pods
sudo kubectl get deployments
```

📸 Captura:

![verificar](https://github.com/PPS10711021/RA5/blob/main/RA5_4/assets/verificar.png)

Instalación y ejecución de Kubernetes.

```bash
curl -sS https://webinstall.dev/k9s | bash
source ~/.config/envman/PATH.env
k9s
```

📸 Captura:

![k9s](https://github.com/PPS10711021/RA5/blob/main/RA5_4/assets/k9s.png)
![k9s2](https://github.com/PPS10711021/RA5/blob/main/RA5_4/assets/k9s2.png)

---

### 🔧 5.2 – Despliegue en modo HA

- ✅ Instalar K3s en modo Alta Disponibilidad  
- ✅ Base de datos embebida (etcd) o externa  
- ✅ Validación con kubectl y K9s  
- 📸 Capturas: arquitectura HA, validación

Instalación inicial en modo HA.

```bash
curl -sfL https://get.k3s.io | INSTALL_K3S_EXEC="server --cluster-init" sh -
```

📸 Captura:

![k9s3](https://github.com/PPS10711021/RA5/blob/main/RA5_4/assets/k9s3.png)

Obtenemos el token del nodo lider.

```bash
sudo cat /var/lib/rancher/k3s/server/node-token
```

📸 Captura:

![k9s4](https://github.com/PPS10711021/RA5/blob/main/RA5_4/assets/k9s4.png)

Despliegue del servicio nginx (modo HA).

```bash
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ha-nginx-deployment
spec:
  replicas: 2
  selector:
    matchLabels:
      app: ha-nginx
  template:
    metadata:
      labels:
        app: ha-nginx
    spec:
      containers:
      - name: nginx
        image: nginx:alpine
        ports:
        - containerPort: 80
```

```bash
sudo kubectl apply -f ha_nginx_deployment.yml
sudo kubectl get pods
```

📸 Captura:

![k9s5](https://github.com/PPS10711021/RA5/blob/main/RA5_4/assets/k9s5.png)

---

### 🔧 5.3 – Despliegue multi-contenedor con Docker Compose

URL:  
📎 [Taller de Docker: Balanceo de carga](https://aulasoftwarelibre.github.io/taller-de-docker/dockerfile/#balanceo-de-carga)

- ✅ Deploy desde Compose adaptado a Kubernetes  
- ✅ Validación con K9s  
- 📸 Capturas: servicio Flask + Redis + Traefik desplegado, estado en K9s

Archivo docker-compose.

```bash
version: "3"
services:
  web1:
    image: nginx
  web2:
    image: nginx
  balanceador:
    image: nginx
    ports:
      - "8080:80"
```

📸 Captura:

![compose](https://github.com/PPS10711021/RA5/blob/main/RA5_4/assets/compose.png)

Conversión a manifiestos Kubernetes con Kompose.

```bash
kompose convert
```

📸 Captura:

![kompose](https://github.com/PPS10711021/RA5/blob/main/RA5_4/assets/kompose.png)

Exposición del balanceador nginx.

```bash
sudo kubectl apply -f balanceador-service.yaml
```

📸 Captura:

![balancer](https://github.com/PPS10711021/RA5/blob/main/RA5_4/assets/balancer.png)

Verificación del balanceador.

```bash
sudo kubectl get pods
sudo kubectl get svc
sudo curl http://192.168.1.129:30000
```

📸 Captura:

![curl](https://github.com/PPS10711021/RA5/blob/main/RA5_4/assets/cuel.png)

---

## ✅ Conclusión

Esta práctica ha permitido:

- 🔹 Desplegar clústeres K3s en modo Single y HA  
- 🔹 Desplegar y escalar servicios como `nginx`  
- 🔹 Integrar herramientas CLI (kubectl) y TUI (K9s)  
- 🔹 Aprender arquitectura de orquestación y automatización  
- 🔹 Trabajar en entornos reales con herramientas de DevOps

---

## 🗂️ Requisitos de entrega

Entrega en carpeta comprimida o repositorio con:

- ✔️ Capturas de kubectl mostrando pods y servicios  
- ✔️ Capturas de K9s validando los despliegues  
- ✔️ Evidencias de despliegue nginx (Single y HA)  
- ✔️ Configuraciones utilizadas (.yaml)  
- ✔️ Despliegue docker-compose adaptado a Kubernetes  
- ✔️ Documento explicativo con los pasos reproducidos

---

## 📖 Referencias

- 🔗 [Kubernetes.io](https://kubernetes.io/es/)  
- 🔗 [K3s.io](https://k3s.io/)  
- 🔗 [K9sCLI.io](https://k9scli.io/)  
- 📝 [Taller Docker: Balanceo de carga](https://aulasoftwarelibre.github.io/taller-de-docker/dockerfile/#balanceo-de-carga)
