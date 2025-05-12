# 🚀 Automatización y Despliegue Seguro con Jenkins – CI/CD Practices

## 📌 Introducción

### 🔄 1.1. CI/CD – Integración y Despliegue Continuo
La automatización en el desarrollo de software moderno es fundamental para entregar código de calidad de manera rápida y segura. El modelo **CI/CD (Continuous Integration / Continuous Deployment)** se basa en prácticas que permiten:

✅ Integrar cambios de código constantemente en un repositorio compartido  
✅ Automatizar la construcción, pruebas y despliegue del software  
✅ Reducir errores humanos mediante pipelines reproducibles  
✅ Detectar fallos a tiempo y facilitar despliegues controlados en producción

### ⚙️ 1.2. Jenkins – Automatización en Acción
**Jenkins** es una herramienta open-source escrita en Java que permite implementar procesos CI/CD de forma flexible y extensible. Mediante su arquitectura basada en plugins, Jenkins permite:

- 🔹 Integrarse con sistemas de control de versiones (Git)  
- 🔹 Ejecutar pruebas automáticas, builds y despliegues  
- 🔹 Definir flujos con archivos `Jenkinsfile` (pipeline como código)  
- 🔹 Trabajar en entornos virtualizados o contenerizados (Docker)  
- 🔹 Monitorizar tareas desde una interfaz web intuitiva

### 📄 1.3. Jenkinsfile y Docker
Gracias al uso de Jenkinsfile, los procesos de integración y despliegue quedan versionados y automatizados. Además, con el uso de Docker y Docker Compose, es posible:

✅ Crear entornos consistentes para pruebas  
✅ Generar imágenes y contenedores desde Jenkins  
✅ Automatizar el ciclo completo de desarrollo ➝ test ➝ despliegue

---

## 🎯 Objetivos

Esta práctica permite alcanzar los siguientes criterios del módulo de *Ciberseguridad en entornos de las tecnologías de la información*:

### 📌 RA5: Implanta sistemas seguros de despliegue de software, utilizando herramientas para la automatización de la construcción de sus elementos.

- ✔ **CA.A:** Configuración y uso de Jenkins para CI/CD  
- ✔ **CA.B:** Automatización de pruebas y despliegues  
- ✔ **CA.C:** Integración segura con entornos Docker  
- ✔ **CA.D:** Definición de pipelines como código (Jenkinsfile)  
- ✔ **CA.E:** Generación y ejecución de imágenes y contenedores  
- ✔ **CA.F:** Control de versiones y documentación en GitHub

---

## 🛠️ Actividades

### ✅ 3.1. Primeros pasos con Jenkins
- 🔧 Realizar las tareas 1 y 2 del apartado de Jenkins disponibles en:  
  [Guía de Jenkins – Tareas](https://psegarrac.github.io/Ciberseguridad-PePS/tema5/cd/ci/2022/01/13/jenkins.html#tareas)  
- 📄 Crear y ejecutar una pipeline básica mediante `Jenkinsfile`

### ✅ 3.2. Jenkins + Docker: Automatización avanzada
- 🔄 Crear un `jenkinsfile.docker` que incluya:

  1️⃣ **Stage:** Construcción de la imagen Docker  
  2️⃣ **Stage:** Ejecución de contenedor desde la imagen  
  3️⃣ **Stage:** Ejecución de tests dentro del contenedor  
  4️⃣ **Stage:** Despliegue automatizado  
  5️⃣ **Stage:** Docker Compose con múltiples servicios

📁 Todo el proyecto debe estar correctamente organizado en GitHub, incluyendo un **README** con capturas de las pipelines y una breve explicación de su funcionamiento.

---

## 📦 Requisitos de entrega

📂 Entrega mediante repositorio GitHub:  
- ✔️ `Jenkinsfile` y `jenkinsfile.docker`  
- ✔️ `docker-compose.yml`  
- ✔️ README con capturas y descripción  

✍️ Informe detallado con:  
- 🔍 Explicación de cada etapa del pipeline  
- 📸 Evidencias visuales  
- 🔐 Medidas de seguridad implementadas

---

## 📖 Referencias

- 🌐 [Jenkins Official Site](https://www.jenkins.io)  
- 📘 [Using Docker with Jenkins Pipelines](https://www.jenkins.io/doc/book/pipeline/docker/)  
- 💻 [Repositorio Jenkins – Ejemplos](https://github.com/jenkinsci/pipeline-examples)

