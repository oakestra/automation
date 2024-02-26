# How to automate Oakestra deployment using Ansible Playbooks

Table of content:
- [🪛Prerequisites🪛](#Prerequisites)
- [🌳Root and Cluster Orchestrators🌳](#Root-and-Cluster-Orchestrators)
	- [🌱 1 DOC (1 Device One Cluster)](#-1-DOC-1-Device-One-Cluster)
	- [🌳 Setup with full Root and Clusters hierarchy](#-Setup-with-full-Root-and-Clusters-hierarchy)
	- [💀 Kill all Root and Cluster instances](#-Kill-all-Root-and-Cluster-instances)
- [👷‍♀️Worker Nodes👷](#Worker-Nodes)
	- [⚙️ Install worker node components](#-Install-worker-node-components)
	- [🟢 (Re)Start worker nodes](#-ReStart-worker-nodes)
	- [💀 Kill worker nodes](#-Kill-worker-nodes)

## 🪛Prerequisites🪛
Make sure to install the following:
- apt install ansible
- pip install Jinja2
- pip install psutil

install ansible dependencies with `ansible-galaxy install -r requirements.yml`

## 🌳Root and Cluster Orchestrators🌳

### 🌱 1 DOC (1 Device One Cluster)

In this section, we'll see how to automate the deployment of the root and cluster orchestrator in 1-DOC setup. Therefore, root and cluster orchestrator will run on the same machine. 
Let's start by describing our [onedoc.yml inventory file](/ansible/inventory_templates/onedoc.yml). This is a description of the root machine where we'll run our components. 

Don't forget to replace the <KEYWORDS> accordingly and copy your configured inventory file into the [inventories](/ansible/inventories/) directory.
N.b. it is better to avoid ssh username and password and aither use a [vault](https://docs.ansible.com/ansible/latest/tips_tricks/ansible_tips_tricks.html#tip-for-variables-and-vaults) or [ssh keys](https://docs.ansible.com/ansible/latest/inventory_guide/intro_inventory.html#connecting-to-hosts-behavioral-inventory-parameters). 

Then, if you have [ansible-playbook](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html) installed and configured, simply run:

```
ansible-playbook playbooks/start-1-DOC.yml
```

This command will clone oakestra repo and startup cluster and root orchestrator on the same `root` machine you defined. 

You can check the component logs inside the target machine using:
```
docker compose -f ~/oakestra_ansible/run-a-cluster/1-DOC.yaml logs
```

### 🌳 Setup with full Root and Clusters hierarchy

Similarly as 1-DOC, let's start with [oakestra.yml inventory file](/ansible/inventory_templates/oakestra.yml). 

Don't forget to replace the <KEYWORDS> accordingly and copy your configured inventory file into the [inventories](/ansible/inventories/) directory.
N.b. it is better to avoid ssh username and password and aither use a [vault](https://docs.ansible.com/ansible/latest/tips_tricks/ansible_tips_tricks.html#tip-for-variables-and-vaults) or [ssh keys](https://docs.ansible.com/ansible/latest/inventory_guide/intro_inventory.html#connecting-to-hosts-behavioral-inventory-parameters). 

Then, if you have [ansible-playbook](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html) installed and configured, simply run:

```
ansible-playbook playbooks/start-full-root-and-clusters.yml
```

This command will clone oakestra repo and startup the root orchestrator component and the all the cluster as described in the inventory above. 

You can check the root logs inside the target machine using:
```
cd oakestra/root_orchestrator ; docker compose logs 
```
and the cluster logs inside the target machines by using:
```
cd oakestra/cluster_orchestrator ; docker compose logs
```

### 💀 Kill all Root and Cluster instances

Given the inventory file that you used earlier, we'll here reference it as `inventory.yml`

Run the following to kill all root and cluster instances (it works for both 1-DOC and full deployment)

```
ansible-playbook playbooks/kill-all-root-and-clusters.yml
```

## 👷‍♀️Worker Nodes👷

If you have your Root and Cluster orchestrator(s) component(s) running, you now just need to attach some worker nodes! 

### 📝 Worker node's inventory 

Let's configure the [workers.yml inventory file](/ansible/inventory_template/workers.yml). 

### ⚙️ Install worker node components 

If you have [ansible-playbook](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html) installed and configured, simply run:

```
ansible-playbook playbooks/install-worker-nodes.yml
```

This will install and configure the `NodeEngine` and `NetworkManager` components on all the machines in your inventory. 

### 🟢 (Re)Start worker nodes

This script will start (or, if already running, re-start) all your worker nodes. 

If you have [ansible-playbook](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html) installed and configured, simply run:

```
ansible-playbook playbooks/restart-nodes.yml
```

This will start the  `NodeEngine` and `NetworkManager` components. The logs are available respectively in `\etc\nodeengine.log` and `\etc\netmanager.log` in the target machines. 

### 💀 Kill worker nodes

This script will kill all your worker nodes. 

If you have [ansible-playbook](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html) installed and configured, simply run:

```
ansible-playbook playbooks/kill-nodes.yml
```

This will kill the  `NodeEngine` and `NetworkManager` components on all nodes.  





