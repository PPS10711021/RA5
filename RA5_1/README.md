# 🚀 Jenkins CI/CD - Seguridad en Despliegue Automatizado

## 📌 Introducción

### 🔄 1.1. Automatización CI/CD  
La integración y el despliegue continuo (CI/CD) representan un pilar clave en la entrega ágil y segura de software. Automatizar estos procesos permite reducir errores humanos, mejorar la calidad del código y acelerar la entrega de nuevas funcionalidades. Los objetivos principales de CI/CD son:

✅ Compilación y pruebas automatizadas  
✅ Integración continua de cambios  
✅ Despliegue rápido, trazable y seguro  
✅ Reversión rápida ante errores

### 🛠️ 1.2. Jenkins como motor de automatización  
**Jenkins** es una herramienta open-source utilizada para automatizar tareas relacionadas con el desarrollo, prueba y despliegue de aplicaciones. Es altamente personalizable y extensible mediante plugins.

🔹 Soporte para integración con Git, Docker, Maven, Kubernetes  
🔹 Definición de pipelines mediante Jenkinsfile  
🔹 Monitoreo a través de interfaz web  
🔹 Ejecución en servidores físicos, virtuales o contenedores  
🔹 Pipeline as Code: versión controlada de los procesos

### 📄 1.3. Jenkinsfile y Docker  
Un `Jenkinsfile` permite describir de forma programática el flujo de trabajo de una pipeline. Al integrarlo con Docker, se puede construir y ejecutar software en entornos controlados, seguros y repetibles.

🔹 Construcción de imágenes Docker  
🔹 Ejecución de tests dentro de contenedores  
🔹 Despliegue de aplicaciones desde la pipeline  
🔹 Uso de `docker-compose` para servicios multi-contenedor

---

## 🎯 Objetivos

Esta práctica permite alcanzar los siguientes criterios de evaluación:

📌 **RA5:** Implanta sistemas seguros de despliegue de software utilizando herramientas de automatización.

✔ **CA.A:** Uso de Jenkins para automatización de pipelines  
✔ **CA.B:** Integración de Jenkins con Docker  
✔ **CA.C:** Ejecución segura de pruebas y despliegues  
✔ **CA.D:** Uso de control de versiones (GitHub)  
✔ **CA.E:** Documentación del proceso y evidencias

---

## 🛠️ Actividades

### ✅ 3.1. Requisitos previos  
🔗 Crear cuenta en **GitHub** para entregar el repositorio con el código y pipelines.  
📦 Crear cuenta en **Docker Hub** para almacenar imágenes, si se requiere.  

### 🔧 3.2. Pipeline básico con Jenkins  
📄 Crear un pipeline utilizando un `Jenkinsfile` que compile y despliegue una aplicación de prueba.

📖 Referencia: [Tareas Jenkins](https://psegarrac.github.io/Ciberseguridad-PePS/tema5/cd/ci/2022/01/13/jenkins.html#tareas)

### 🐳 3.3. Jenkins + Docker  
📌 Crear un `jenkinsfile.docker` que incluya los siguientes stages:

1️⃣ **Build Docker:** Construcción de imagen desde Dockerfile  
2️⃣ **Run Container:** Ejecución del contenedor  
3️⃣ **Run Tests:** Ejecución de pruebas dentro del contenedor  
4️⃣ **Deploy:** Simulación o ejecución real de despliegue  
5️⃣ **Docker Compose:** Lanzamiento de servicios mediante `docker-compose`

---

## 📦 Requisitos de entrega

📂 Entrega mediante repositorio GitHub con:

✔️ `Jenkinsfile`  
✔️ `jenkinsfile.docker`  
✔️ `docker-compose.yml`  
✔️ `Dockerfile` (si aplica)  
✔️ Capturas de pantalla del funcionamiento de las pipelines  
✔️ README explicando cada etapa del proceso

✍️ Informe detallado que incluya:

- 📸 Evidencias visuales de las ejecuciones  
- 🔍 Descripción técnica de cada fase de la pipeline  
- 🔐 Medidas de seguridad implementadas

---

## 📖 Referencias

- 🌐 [Jenkins Official](https://www.jenkins.io)  
- 📘 [Docker en Jenkins Pipelines](https://www.jenkins.io/doc/book/pipeline/docker/)  
- 💻 [Ejemplos de Jenkinsfile](https://github.com/jenkinsci/pipeline-examples)
