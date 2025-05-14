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

### 🔧 3.1. Realizar las tareas 1 y 2 del apartado de Jenkins  

### Tarea1
[Calculadora](https://github.com/PPS10711021/RA5/blob/main/RA5_1/calculadora.py)
```python
import sys

class Calculadora:
    def multiplicar(self, a, b):
        return a * b

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python calculadora.py <num1> <num2>")
        sys.exit(1)

    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        calc = Calculadora()
        resultado = calc.multiplicar(num1, num2)
        print(f"Resultado: {resultado}")
    except ValueError:
        print("Por favor ingresa dos números válidos.")
        sys.exit(1)
```

[TestCalculadora](https://github.com/PPS10711021/RA5/blob/main/RA5_1/test_calculadora.py)
```python
import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    def setUp(self):
        self.calc = Calculadora()

    def test_multiplicacion_positiva(self):
        self.assertEqual(self.calc.multiplicar(3, 4), 12)

    def test_multiplicacion_cero(self):
        self.assertEqual(self.calc.multiplicar(0, 100), 0)

    def test_multiplicacion_negativa(self):
        self.assertEqual(self.calc.multiplicar(-2, 5), -10)

if __name__ == "__main__":
    unittest.main()
```

Ejecutamos la calculadora y las pruebas unitarias con python3 desde un linux mint:
```
python3 calculadora.py 2 4
python3 -m unittest test_calculadora.py
```
📸 Captura:

![Prueba Calculadora y Test](https://github.com/PPS10711021/RA5/blob/main/RA5_1/assets/calc.png)

### Tarea2
📄 Crear un pipeline utilizando un `Jenkinsfile` que compile y despliegue una aplicación de prueba.

[Jenkinsfile](https://github.com/PPS10711021/RA5/blob/main/RA5_1/Jenkinsfile)
```python
pipeline {
    agent any

    triggers {
        pollSCM('* * * * *')
    }

    stages {
        stage('Preparar entorno') {
            steps {
                echo 'Entorno listo para pruebas.'
            }
        }

        stage('Pruebas Unitarias') {
            steps {
                sh 'PYTHONPATH=RA5_1 python3 -m unittest RA5_1/test_calculadora.py'
            }
        }
    }

    post {
        success {
            echo 'Pipeline ejecutado correctamente.'
        }
        failure {
            echo 'La pipeline ha fallado. Revisar errores.'
        }
    }
}
```
Una vez hecho el Jenkinsfile y unido el jenkins con nuestro repositorio, cada vez que haya un commit en el repositorio, pasará por jenkins.

📸 Captura:

![Pipeline correcta](https://github.com/PPS10711021/RA5/blob/main/RA5_1/assets/pipeline_correcta.png)

Una vez funciona todo correctamente, tenemos que comprometer el código y observar lo que sucede, para ello en la calculadora voy a cambiar la multiplicación de "a*b" por "0/b".

📸 Captura:

![MalCodigo](https://github.com/PPS10711021/RA5/blob/main/RA5_1/assets/calc_mal.png)

📸 Captura:

![ErrorPipeline](https://github.com/PPS10711021/RA5/blob/main/RA5_1/assets/error_calc.png)

Por último volvemos a cambiar el código de la calculadora como estaba.

📖 Referencia: [Tareas Jenkins](https://psegarrac.github.io/Ciberseguridad-PePS/tema5/cd/ci/2022/01/13/jenkins.html#tareas)

### 🐳 3.2. Jenkins + Docker  
📌 Crear un `jenkinsfile.docker` que incluya los siguientes stages:

1️⃣ **Build Docker:** Construcción de imagen desde Dockerfile  
2️⃣ **Run Container:** Ejecución del contenedor  
3️⃣ **Run Tests:** Ejecución de pruebas dentro del contenedor  
4️⃣ **Deploy:** Simulación o ejecución real de despliegue  
5️⃣ **Docker Compose:** Lanzamiento de servicios mediante `docker-compose`


Para esta parte tenemos que crear los siguientes archivos, Dockerfile, docker-compose.yml y jenkinsfile.docker:

[Dockerfile](https://github.com/PPS10711021/RA5/blob/main/RA5_1/Dockerfile)
```
FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install --upgrade pip

CMD ["python3", "-m", "unittest", "test_calculadora.py"]
CMD ["tail", "-f", "/dev/null"]
```

[docker-compose.yml](https://github.com/PPS10711021/RA5/blob/main/RA5_1/docker-compose.yml)
```
version: '3.8'

services:
  calculadora:
    build: .
    container_name: calculadora-compose
    command: python3 -m unittest test_calculadora.py
    volumes:
      - .:/app
    working_dir: /app
```

[jenkinsfile.docker](https://github.com/PPS10711021/RA5/blob/main/RA5_1/jenkinsfile.docker)
```
pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                dir('RA5_1') {
                    sh 'docker build -t calculadora-image .'
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                dir('RA5_1') {
                    sh 'docker rm -f calculadora-container || true'
                    sh 'docker run --name calculadora-container -d calculadora-image'
                }
            }
        }

        stage('Run Tests in Docker') {
            steps {
                dir('RA5_1') {
                    sh 'docker exec calculadora-container python3 -m unittest test_calculadora.py'
                }
            }
        }

        stage('Stop Docker Container') {
            steps {
                dir('RA5_1') {
                    sh 'docker stop calculadora-container && docker rm calculadora-container'
                }
            }
        }

        stage('Docker Compose Up') {
            steps {
                dir('RA5_1') {
                    sh 'docker-compose up -d'
                }
            }
        }

        stage('Docker Compose Down') {
            steps {
                dir('RA5_1') {
                    sh 'docker-compose down'
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline Docker ejecutada correctamente.'
        }
        failure {
            echo 'Falló la pipeline Docker.'
        }
    }
}
```
Una vez tenemos estos archivos, conseguimos que:
-Al hacer un push en GitHub, el webhook lo notifica a Jenkins.
-Jenkins toma el archivo jenkinsfile.docker.
-Ejecuta:
    -Build de imagen Docker
    -Contenedor Docker
    -Tests dentro del contenedor
    -Apaga el contenedor
    -Prueba docker-compose up/down

### Ahora configuraremos el webhook con ngrok
Cuando hacemos un push en GitHub, el webhook necesita una URL pública a la que enviar la notificación.
Pero como Jenkins está corriendo localmente en nuestra máquina (localhost:8080), GitHub no puede alcanzarlo directamente.
Ngrok crea un túnel seguro que expone tu Jenkins en una URL pública.

📸 Captura:

![ultima1.png](https://github.com/PPS10711021/RA5/blob/main/RA5_1/assets/ultima1.png)

Aquí ponemos en marcha ngrok, y ahora pondremos la url pública en el webhook de github.

📸 Captura:

![ultima3.png](https://github.com/PPS10711021/RA5/blob/main/RA5_1/assets/ultima3.png)

Aquí verificamos que ngrok está activo y que GitHub ha enviado correctamente una solicitud POST al webhook. El código de estado 200 OK indica que Jenkins recibió y procesó la solicitud sin errores.

📸 Captura:

![ultima5.png](https://github.com/PPS10711021/RA5/blob/main/RA5_1/assets/ultima5.png)

Por último esta imagen muestra que la ejecución de la pipeline Jenkins ha sido exitosa, iniciada por un push de GitHub (trigger automático). Esto confirma que el webhook está funcionando correctamente y Jenkins ha obtenido el jenkinsfile.docker desde GitHub.

📸 Captura:

![ultima6.png](https://github.com/PPS10711021/RA5/blob/main/RA5_1/assets/ultima6.png)

---

## ✅ Conclusión

Esta práctica ha permitido implementar de forma completa un entorno de **CI/CD automatizado y seguro** utilizando **Jenkins** y **Docker**, aplicando los conceptos fundamentales del desarrollo seguro y continuo. Se ha diseñado una solución funcional que:

- 🔹 Automatiza el testeo y despliegue de una aplicación Python  
- 🔹 Utiliza `Jenkinsfile` para definir pipelines reproducibles  
- 🔹 Integra Docker para asegurar entornos controlados  
- 🔹 Ejecuta pruebas unitarias dentro de contenedores  
- 🔹 Orquesta contenedores con `docker-compose`  
- 🔹 Automatiza la ejecución mediante Webhooks y `ngrok`  

Además, se ha trabajado con herramientas reales del entorno profesional, resolviendo problemas habituales como la exposición segura del entorno local o los permisos del demonio Docker dentro de Jenkins. El resultado final demuestra que es posible automatizar todo el flujo desde un commit en GitHub hasta el testeo y despliegue en contenedores, reforzando la trazabilidad, la seguridad y la eficiencia del desarrollo software.

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
