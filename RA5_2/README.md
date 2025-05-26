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

El primer paso de la práctica consistió en el provisionamiento automático de una máquina virtual Ubuntu 22.04 (Jammy) mediante el uso de Vagrant y VirtualBox.
Utilizamos el comando:
```python
vagrant up
```
```python
Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/jammy64"
  config.vm.hostname = "ansible-node"

  config.vm.network "private_network", ip: "192.168.100.10"

  config.vm.provider "virtualbox" do |vb|
    vb.name = "ubuntu-ansible"
    vb.memory = 2048
    vb.cpus = 2
  end

  config.vm.provision "shell", inline: <<-SHELL
    apt-get update
    apt-get install -y python3 python3-pip
  SHELL
end
```
📸 Captura:

![VagrantUp](https://github.com/PPS10711021/RA5/blob/main/RA5_2/assets/vagrant1.png)

La máquina se inició sin errores y quedó preparada para la fase de automatización con Ansible. La red privada configurada funcionó correctamente, y se confirmó el acceso por SSH mediante clave privada.

En la siguiente imagen observamos la máquina creada en VirtualBox.

📸 Captura:

![Creada](https://github.com/PPS10711021/RA5/blob/main/RA5_2/assets/creada.png)

### 🔧 3.2. Configuración inicial con Ansible

📄 Automatizar con un **playbook**:

- `update` y `upgrade` del sistema
- Instalación de **Apache**

Creamos el archivo inventory.ini y el playbook_update_apache.yml:
```python
[web]
192.168.100.10 ansible_user=vagrant ansible_ssh_private_key_file=/vagrant/.vagrant/machines/default/virtualbox/private_key ansible_python_interpreter=/usr/bin/python3
```
```python
---
- name: Actualizar sistema e instalar Apache
  hosts: web
  become: true

  tasks:
    - name: Actualizar lista de paquetes
      apt:
        update_cache: yes

    - name: Actualizar todos los paquetes
      apt:
        upgrade: dist

    - name: Instalar Apache2
      apt:
        name: apache2
        state: present
```
📸 Accedemos por ssh a la máquina:

![ssh](https://github.com/PPS10711021/RA5/blob/main/RA5_2/assets/vagrantssh.png)

```python
vagrant ssh
```

📸 Instalamos ansible:

![InstalarAnsible](https://github.com/PPS10711021/RA5/blob/main/RA5_2/assets/ansible.png)

```python
sudo apt install -y ansible
```

📸 Captura de ejecución correcta del playbook:

![PlaybookApache](https://github.com/PPS10711021/RA5/blob/main/RA5_2/assets/ansible2.png)

```python
ansible-playbook -i inventory.ini playbook_update_apache.yml
```

### 💻 3.3. Personalización y validación del servidor web

📄 Con otro playbook:

- Crear un archivo `index.html` con contenido **"Ansible rocks"**
- Reiniciar Apache
- Ejecutar `curl` y comprobar el mensaje

Creamos el archivo playbook_index_html.yml:
```python
---
- name: Configurar index.html y reiniciar Apache
  hosts: web
  become: true

  tasks:
    - name: Crear archivo index.html con contenido
      copy:
        dest: /var/www/html/index.html
        content: "Ansible rocks"

    - name: Reiniciar Apache
      service:
        name: apache2
        state: restarted

    - name: Verificar contenido con curl
      shell: "curl -s http://localhost"
      register: result

    - name: Mostrar resultado de curl
      debug:
        var: result.stdout
```

📸 Captura del resultado de la ejecución del playbook.

![PlaybookApache](https://github.com/PPS10711021/RA5/blob/main/RA5_2/assets/ansible3.png)

```python
ansible-playbook -i inventory.ini playbook_index_html.yml
```
En la imagen se observa que todas las tareas se ejecutaron correctamente (ok=5, failed=0) y que el resultado del curl es exactamente "Ansible rocks", confirmando que el despliegue web fue exitoso.

La ejecución del playbook demuestra que Ansible puede automatizar de forma efectiva la configuración de servicios web, garantizando que el contenido deseado se despliegue y esté disponible desde el navegador o herramientas como curl.
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
