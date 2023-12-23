HOW TO DEPLOY APPLICATION TO SERVER
---
## Build installation-playbooks
> mvn clean install -Dpassword=<your_jfrog_password> -Drevision=<playbooks_version>

## Download installation-playbooks from Jfrog artifactory
> wget https://phongnghia.jfrog.io/artifactory/default-generic-local/installation-playbooks-<package_version>.zip

## Run installation-playbooks to deploy application
> [!NOTE]
> To be able to run ***ansible-playbook*** command, you need to install the following necessary packages: ***ansible, sshpass***

### Command 
**Install Kubernetes and myresume app**
> ansible-playbook install.yml
**Install with skip-tags option
> ansible-playbook install.yml --skip-tags "*<tag_name>*"
>
Example:
>ansible-playbook install.yml --skip-tags "pre-install,kubernetes"
