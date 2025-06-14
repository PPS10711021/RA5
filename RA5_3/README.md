# 📊 Monitorización de Infraestructura con Prometheus y Grafana – RA5.3

## 📌 Introducción

### 🔍 1.1. ¿Qué es un sistema de monitorización?

Un **sistema de monitorización informática** permite observar el estado y rendimiento de recursos tecnológicos (servidores, servicios, redes, etc.) en tiempo real. Facilita la **detección proactiva de fallos**, mejora la disponibilidad y refuerza la seguridad operativa de la infraestructura.

✅ Recolección de métricas del sistema  
✅ Almacenamiento y visualización en dashboards  
✅ Notificaciones ante eventos o fallos  
✅ Análisis de logs y comportamiento del sistema  

---

### 🧠 1.2. Prometheus

**Prometheus** es una herramienta open source de recolección y almacenamiento de métricas basada en series temporales. Su función principal es **scrapear** endpoints HTTP expuestos por servicios como *node_exporter* para recopilar métricas del sistema.

🔹 Almacenamiento interno optimizado  
🔹 Lenguaje de consulta PromQL  
🔹 Integración con Grafana  
🔹 Detección de targets y alertas  

---

### 📈 1.3. Grafana

**Grafana** permite **visualizar** métricas desde múltiples fuentes (como Prometheus) mediante paneles personalizables. Es muy usada en entornos DevOps, ciberseguridad y administración de sistemas.

🔹 Paneles interactivos y personalizables  
🔹 Soporte para múltiples orígenes de datos  
🔹 Alertas visuales y por email/Slack  
🔹 Comunidad activa y dashboards compartidos  

---

## 🎯 Objetivos

Esta práctica trabaja los siguientes criterios de evaluación:

📌 **RA5**: Analizar incidentes de ciberseguridad utilizando herramientas, mecanismos de detección y alertas de seguridad.

✔ **CA5.A**: Identificación y configuración de herramientas de monitorización  
✔ **CA5.B**: Integración de métricas del sistema en dashboards  
✔ **CA5.C**: Evaluación gráfica del estado de la infraestructura

---

## 🛠️ Actividades

### 🔧 3.1. Validar el stack Prometheus + Grafana

📄 Siguiendo el repositorio de ejemplo:

- [Repositorio oficial](https://github.com/dinesh24murali/example_repo/tree/main/prometheus_grafana_example)
- [Artículo explicativo](https://medium.com/@dineshmurali/introduction-to-monitoring-with-prometheus-grafana-ea338d93b2d9)

📸 Se realizaron capturas de:

- Prometheus funcionando en `http://localhost:9090`
- Dashboard de Grafana en `http://localhost:3000`
- Conexión entre Grafana y Prometheus

---

### 🖥️ 3.2. Implementación del sistema de monitorización personalizado

#### 🛡️ Servidor Ubuntu (Node Exporter)

📄 Instalamos `node_exporter` en **Ubuntu Server** para exponer métricas del sistema:

```bash
wget https://github.com/prometheus/node_exporter/releases/latest/download/node_exporter-1.8.0.linux-amd64.tar.gz
tar xvfz node_exporter-1.8.0.linux-amd64.tar.gz
sudo cp node_exporter-1.8.0.linux-amd64/node_exporter /usr/local/bin/
```

---

Clonamos el repositorio

```bash
git clone https://github.com/dinesh24murali/example_repo.git
cd example_repo/prometheus_grafana_example
```

Instalar node exporter

```bash
wget https://github.com/prometheus/node_exporter/releases/download/v1.9.1/node_exporter-1.9.1.linux-amd64.tar.gz
```

Copiamos el binario

```bash
tar -xvzf node_exporter-1.9.1.linux-amd64.tar.gz
cd node_exporter-1.9.1.linux-amd64
sudo cp node_exporter /usr/local/bin/
```

Creamos el servicio systemd

```bash
# /etc/systemd/system/node_exporter.service
[Unit]
Description=Node Exporter
After=network.target

[Service]
User=root
ExecStart=/usr/local/bin/node_exporter

[Install]
WantedBy=default.target
```

Docker compose build y up

```bash
docker-compose build
docker-compose up -d
```
Capturas:
![Build](https://github.com/PPS10711021/RA5/blob/main/RA5_3/assets/pro1.png)
![Up](https://github.com/PPS10711021/RA5/blob/main/RA5_3/assets/docker-composeup.png)

cAdvisor funciona en http://localhost:8080 y nos da información del sistema.

Capturas:
![cadvisor](https://github.com/PPS10711021/RA5/blob/main/RA5_3/assets/cadvisor.png)

Grafana funcionando en http://localhost:3000 y mostrando métricas.

Capturas:
![grafana](https://github.com/PPS10711021/RA5/blob/main/RA5_3/assets/grafana.png)
![grafana2](https://github.com/PPS10711021/RA5/blob/main/RA5_3/assets/grafana2.png)

Prometheus funcionando y mostrando información.

Capturas:
![pro2](https://github.com/PPS10711021/RA5/blob/main/RA5_3/assets/pro2.png)
![targets](https://github.com/PPS10711021/RA5/blob/main/RA5_3/assets/targets.png)

Servicio de node_exporter corriendo en el servidor remoto.

```bash
sudo systemctl status node_exporter
```
Capturas:
![servicio_node](https://github.com/PPS10711021/RA5/blob/main/RA5_3/assets/servicio_node.png)

---

## ✅ Conclusión

Esta práctica ha permitido:

🔹 Implementar un sistema de monitorización completo  
🔹 Recoger métricas del sistema con Node Exporter  
🔹 Almacenar y visualizar métricas con Prometheus y Grafana  
🔹 Verificar visualmente el estado del sistema  
🔹 Reforzar conocimientos sobre detección y análisis de incidentes  
🔹 Comprender la arquitectura cliente-servidor en entornos de observabilidad

Gracias al uso de herramientas open source, se garantiza una solución flexible y escalable para el seguimiento y análisis de infraestructuras TI.

---

## 📦 Requisitos de entrega

📂 Entrega mediante carpeta comprimida o repositorio con:

✔️ Capturas del servidor con `node_exporter` funcionando  
✔️ Capturas de Prometheus accediendo al target remoto  
✔️ Capturas del dashboard de Grafana mostrando las métricas  
✔️ Archivo `prometheus.yml` configurado  
✔️ Evidencia de los servicios activos (`systemctl status`)  
✔️ Documento explicativo (`README.md`) con pasos reproducibles  

💡 *Opcional:* incluir archivo `.service` de node_exporter y `captura del puerto 9100` abierto en el servidor.

---

## 📖 Referencias

- 📘 [Prometheus - Sitio oficial](https://prometheus.io/)  
- 📘 [Grafana - Sitio oficial](https://grafana.com/)  
- 📘 [Node Exporter GitHub](https://github.com/prometheus/node_exporter)  
- 📰 [Artículo de Dinesh Murali en Medium](https://medium.com/@dineshmurali/introduction-to-monitoring-with-prometheus-grafana-ea338d93b2d9)  
- 📦 [Repositorio Prometheus + Grafana](https://github.com/dinesh24murali/example_repo/tree/main/prometheus_grafana_example)
