# Oakestra Automation Helpers

This repo contains automation scripts that help setup and manage Oakestra operations. If you want to push your own automation, please push your updates containing a new folder which contains your code and README.md that explains how to use your scripts.

Please remove any unique identifiers relevant to your setup so that your scripts are usable generally.

## Automation Index

1. [/ansible](/ansible): [Ansible Playbooks](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html) to automate root/cluster orchestrator and worker nodes deployment in your cluster(s). 

2. [/development_cluster_management](/development_cluster_management/): [Development Cluster](https://github.com/oakestra/oakestra?tab=readme-ov-file#%EF%B8%8F-how-to-create-a-development-cluster) management and automations - general development setup

    - [/persistent_multi_terminal_setup](/development_cluster_management/persistent_multi_terminal_setup/): Rebootable TMUX configuration with cluster management scripts

3. [/api](/api): [Oakestra API](https://github.com/oakestra/oakestra?tab=readme-ov-file#%F0%9F%A9%BB-use-the-apis-to-deploy-a-new-application-and-check-clusters-status) automations

    - [/default_application_creation](/api/default_application_creation/):  Login & create a default application with services via default SLA. 

4. [/frontend_ui](/frontend/): [Oakestra Dashboard](https://github.com/oakestra/dashboard) automations

    - [/login_and_create_application](/frontend/login_and_create_application/): Login & create an application automatically in a chrome browser. 
