# 🌐 IaC con Terraform y Ansible - Seguridad en Infraestructura Automatizada

## 📌 Introducción

### 🔄 1.1. Infrastructure as Code (IaC)

La **Infraestructura como Código (IaC)** permite definir y aprovisionar entornos tecnológicos mediante código, lo que reduce errores humanos y facilita la trazabilidad y repetibilidad de entornos. Sus ventajas incluyen:

✅ Automatización del aprovisionamiento  
✅ Control de versiones de la infraestructura  
✅ Revisión y auditoría del código de configuración  
✅ Creación rápida de entornos seguros y escalables  

### ⚙️ 1.2. Terraform

**Terraform**, desarrollado por HashiCorp, permite definir y desplegar infraestructura en múltiples proveedores cloud (AWS, Azure, GCP, etc.) usando un lenguaje declarativo (HCL). Entre sus ventajas destacan:

🔹 Proveedor-agnóstico  
🔹 Declarativo e idempotente  
🔹 Previsualización de cambios con `terraform plan`  
🔹 Modularidad y reutilización  

**🧪 Flujo básico de uso**:
1. Escribir el archivo `.tf`  
2. Inicializar con `terraform init`  
3. Previsualizar con `terraform plan`  
4. Aplicar cambios con `terraform apply`  
5. Destruir infraestructura con `terraform destroy`  

### 🛠️ 1.3. Ansible

**Ansible** automatiza la configuración y gestión de sistemas ya aprovisionados, como instalar servicios, actualizar software o configurar archivos. Usa YAML para definir tareas en *playbooks*.

🔹 Sin agentes: conecta por SSH  
🔹 Fácil de aprender (YAML)  
🔹 Idempotente y reutilizable  
🔹 Ampliamente compatible con nubes y CI/CD  

---

## 🎯 Objetivos

Esta práctica trabaja los siguientes criterios de evaluación:

📌 **RA5**: Implantar sistemas seguros de despliegue con herramientas de automatización.  

✔ **CA.E**: Uso de herramientas de aprovisionamiento (Terraform)  
✔ **CA.F**: Automatización de configuración segura (Ansible)  

---

## 🛠️ Actividades

### ⚙️ 3.1. Provisionamiento con Terraform

📄 Crear una máquina virtual **Ubuntu 24.04** en **VirtualBox** usando un archivo `.tf`.  
📸 Se debe incluir **captura de la consola Terraform** tras `apply`.

### 🔧 3.2. Configuración inicial con Ansible

📄 Automatizar con un **playbook**:

- `update` y `upgrade` del sistema
- Instalación de **Apache**

📸 Captura de ejecución correcta del playbook.

### 💻 3.3. Personalización y validación del servidor web

📄 Con otro playbook:

- Crear un archivo `index.html` con contenido **"Ansible rocks"**
- Reiniciar Apache
- Ejecutar `curl` y comprobar el mensaje

📸 Captura del resultado del `curl` mostrando el mensaje esperado.

---

## ✅ Conclusión

Esta práctica ha permitido:

🔹 Aprender y aplicar IaC en entornos locales  
🔹 Automatizar despliegues con **Terraform**  
🔹 Configurar servidores de forma segura con **Ansible**  
🔹 Validar servicios expuestos (Apache) tras automatización  
🔹 Reforzar conocimientos en aprovisionamiento, scripting y pruebas  

---

## 📦 Requisitos de entrega

📂 Entrega mediante repositorio GitHub con:

✔️ Archivos `.tf` para Terraform  
✔️ Playbooks `.yml` para Ansible  
✔️ Capturas de ejecución exitosa  
✔️ `README.md` explicando cada paso  

📝 Informe adicional con:

🔍 Descripción técnica de cada fase  
📸 Evidencias visuales  
🔐 Medidas de seguridad implementadas  

---

## 📖 Referencias

- [Terraform Docs](https://developer.hashicorp.com/terraform/docs)  
- [Ansible Docs](https://docs.ansible.com/)  
