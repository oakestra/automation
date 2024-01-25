# How to automate Oakestra deployment using Ansible Playbooks

Table of content:

- [🌳Root and Cluster Orchestrators🌳](#Root-and-Cluster-Orchestrators)
	- [🌱 1-DOC (1 Device One Cluster)](#-1-DOC-(1-Device-One-Cluster))
	- [🌳 Setup with full Root and Clusters hierarchy](#-Setup-with-full-Root-and-Clusters-hierarchy)
	- [💀 Kill all Root and Cluster instances](#-Kill-all-Root-and-Cluster-instances)
- [👷‍♀️Worker Nodes👷](#Worker-Nodes)
	- [⚙️ Install worker node components](#Install-worker-node-components)
	- [🟢 (Re)Start worker nodes](#(Re)Start-worker-nodes)
	- [💀 Kill worker nodes](#Kill-worker-nodes)

## 🌳Root and Cluster Orchestrators🌳

###🌱 1-DOC (1 Device One Cluster)

In this section, we'll see how to automate the deployment of the root and cluster orchestrator in 1-DOC setup. Therefore, root and cluster orchestrator will run on the same machine. 
Let's start by describing our `onedoc.yml` inventory file. This is a description of the root machine where we'll run our components. 

Example:

```
root:
  hosts:
    root-orchestrator: 
      ansible_host: '<IP OR HOSTNAME>'
      ansible_ssh_user: '<SSH_USERNAME>''
      ansible_ssh_pass: '<SSH_PASSWORD>'
      ansible_become_password: '<ROOT_PASSWORD>'
      rootIP: '<PUBLIC_IP_OF_THIS_MACHINE>'
      clusterName: '<NAME_OF_THE_CLUSTER>'
      clusterLocation: '<LOCATION_OF_THE_CLUSTER>'
```
don't forget to replace the <KEYWORDS> accordingly. 
N.b. it is better to avoid ssh username and password and aither use a [vault](https://docs.ansible.com/ansible/latest/tips_tricks/ansible_tips_tricks.html#tip-for-variables-and-vaults) or [ssh keys](https://docs.ansible.com/ansible/latest/inventory_guide/intro_inventory.html#connecting-to-hosts-behavioral-inventory-parameters). 

Then, if you have [ansible-playbook](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html) installed and configured, simply run:

```
ansible-playbook -i onedoc.yml -k start-1-DOC.yml
```

This command will clone oakestra repo and startup cluster and root orchestrator on the same `root` machine you defined. 

You can check the component logs inside the target machine using `docker compose -f oakestra/run-a-cluster/1-DOC.yaml logs`

### 🌳 Setup with full Root and Clusters hierarchy

Similarly as 1-DOC, let's start with `oakestra.yml` inventory file. 

```
root:
  hosts:
    root-orchestrator: 
      ansible_host: '<IP OR HOSTNAME>'
      ansible_ssh_user: '<SSH_USERNAME>''
      ansible_ssh_pass: '<SSH_PASSWORD>'
      ansible_become_password: '<ROOT_PASSWORD>'
      rootIP: '<PUBLIC_IP_OF_ROOT_ORCHESTRATOR>'
      
cluster:
  vars:
    rootIP: '<PUBLIC_IP_OF_ROOT_ORCHESTRATOR>'
  hosts:
    cluster-1: 
      ansible_host: '<IP OR HOSTNAME>'
      ansible_ssh_user: '<SSH_USERNAME>''
      ansible_ssh_pass: '<SSH_PASSWORD>'
      ansible_become_password: '<ROOT_PASSWORD>'
    cluster-2: 
      ansible_host: '<IP OR HOSTNAME>'
      ansible_ssh_user: '<SSH_USERNAME>''
      ansible_ssh_pass: '<SSH_PASSWORD>'
      ansible_become_password: '<ROOT_PASSWORD>'
    ...
    cluster-100: 
      ansible_host: '<IP OR HOSTNAME>'
      ansible_ssh_user: '<SSH_USERNAME>''
      ansible_ssh_pass: '<SSH_PASSWORD>'
      ansible_become_password: '<ROOT_PASSWORD>'
```
don't forget to replace the <KEYWORDS> accordingly. 
N.b. it is better to avoid ssh username and password and aither use a [vault](https://docs.ansible.com/ansible/latest/tips_tricks/ansible_tips_tricks.html#tip-for-variables-and-vaults) or [ssh keys](https://docs.ansible.com/ansible/latest/inventory_guide/intro_inventory.html#connecting-to-hosts-behavioral-inventory-parameters). 

Then, if you have [ansible-playbook](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html) installed and configured, simply run:

```
ansible-playbook -i onedoc.yml -k start-full-root-and-clusters.yml
```

This command will clone oakestra repo and startup the root orchestrator component and the all the cluster as described in the inventory above. 

You can check the root logs inside the target machine using `cd oakestra/root_orchestrator ; docker compose logs` and the cluster logs inside the target machines using `cd oakestra/cluster_orchestrator ; docker compose logs`


### 💀 Kill all Root and Cluster instances

Given the inventory file that you used earlier, we'll here reference it as `inventory.yml`

run the following to kill all root and cluster instances (it works for both 1-DOC and full deployment)

```
ansible-playbook -i inventory.yml -k kill-all-root-and-clusters.yml
```

## 👷‍♀️Worker Nodes👷

If you have your Root and Cluster orchestrator(s) component(s) running, you now just need to attach some worker nodes! 

### 📝 Worker node's inventory 

Let's create a `workers.yml` inventory file. 

```
nodes:
  hosts:
    worker-1:
      ansible_host: '<IP OR HOSTNAME>'
      ansible_ssh_user: '<SSH_USERNAME>''
      ansible_ssh_pass: '<SSH_PASSWORD>'
      ansible_become_password: '<ROOT_PASSWORD>'
      clusterIP: '<IP_OF_TARGET_CLUSTER_ORCHESTRATOR>'
      nodeIP: '<IP_OF_THIS_MACHINE_REACHABLE_FROM_OTHER_WORKERS>'
    worker-2:
      ansible_host: '<IP OR HOSTNAME>'
      ansible_ssh_user: '<SSH_USERNAME>''
      ansible_ssh_pass: '<SSH_PASSWORD>'
      ansible_become_password: '<ROOT_PASSWORD>'
      clusterIP: '<IP_OF_TARGET_CLUSTER_ORCHESTRATOR>'
      nodeIP: '<IP_OF_THIS_MACHINE_REACHABLE_FROM_OTHER_WORKERS>'
    ...
    worker-100:
      ansible_host: '<IP OR HOSTNAME>'
      ansible_ssh_user: '<SSH_USERNAME>''
      ansible_ssh_pass: '<SSH_PASSWORD>'
      ansible_become_password: '<ROOT_PASSWORD>'
      clusterIP: '<IP_OF_TARGET_CLUSTER_ORCHESTRATOR>'
      nodeIP: '<IP_OF_THIS_MACHINE_REACHABLE_FROM_OTHER_WORKERS>'
    ...
```

### ⚙️ Install worker node components 

If you have [ansible-playbook](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html) installed and configured, simply run:

```
ansible-playbook -i workers.yml -k install-worker-nodes.yml
```

This will install and configure the `NodeEngine` and `NetworkManager` components on all the machines in your inventory. 

### 🟢 (Re)Start worker nodes

This script will start (or, if already running, re-start) all your worker nodes. 

If you have [ansible-playbook](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html) installed and configured, simply run:

```
ansible-playbook -i workers.yml -k restart-nodes.yml
```

This will start the  `NodeEngine` and `NetworkManager` components. The logs are available respectively in `\etc\nodeengine.log` and `\etc\netmanager.log` in the target machines. 

### 💀 Kill worker nodes

This script will kill all your worker nodes. 

If you have [ansible-playbook](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html) installed and configured, simply run:

```
ansible-playbook -i workers.yml -k kill-nodes.yml
```

This will kill the  `NodeEngine` and `NetworkManager` components on all nodes.  





