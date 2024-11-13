# Automatically create Certficates and Keyfiles for MQTTS connections
These scripts automate certificate file generation for MQTTS.
Make sure the env variable SYSTEM_MANAGER_URL has been set.
Enter desired/specified passwords when prompted.
Execute the scripts in the directory where the files should be created.

This is to be used with the cluster_orchestrator override-mosquitto-auth.yml. More details in the cluster_orchestrator README.

## cluster.sh
This script creates certificate files for the MQTT broker and the cluster_manager.

## node.sh
This script creates certificate files for the NodeEngine.
The envs CA_CRT and CA_KEY containing the paths to the ca.crt and ca.key respectively must be set

