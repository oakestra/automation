# MQTTS Broker
echo "Generating Certificate Authority"
openssl req -new -x509 -days 365 -extensions v3_ca -keyout ca.key -out ca.crt -subj "/C=DE/ST=Bavaria/L=Munich/O=Oakestra/OU=Certificate Authority"
openssl genrsa -out server.key 2048
echo "-------------------------------"

# Check if URL is IPv4
if expr "${SYSTEM_MANAGER_URL}" : '[0-9][0-9]*\.[0-9][0-9]*\.[0-9][0-9]*\.[0-9][0-9]*$' >/dev/null; then
    echo "IPv4 detected"
    openssl req -out server.csr -key server.key -new -addext "subjectAltName = IP:${SYSTEM_MANAGER_URL}, DNS:mqtts" -subj "/C=DE/ST=Bavaria/L=Munich/O=Oakestra/OU=MQTTS\CN=mqtts"
else
    # Check if URL is IPv6
    if [[ "${SYSTEM_MANAGER_URL}" =~ ^\[(\:\:)?[0-9a-fA-F]{1,4}(\:\:?[0-9a-fA-F]{1,4}){0,7}(\:\:)?\]$ ]] && [[ "${SYSTEM_MANAGER_URL}" =~ ^\[.*\:.*\:.*\]$ ]] ; then
        string="${SYSTEM_MANAGER_URL}"
        ipv6=$(echo "${string:1:${#string}-2}")
        echo "IPv6 detected - trimming [...]"
        openssl req -out server.csr -key server.key -new -addext "subjectAltName = IP:${ipv6}, DNS:mqtts" -subj "/C=DE/ST=Bavaria/L=Munich/O=Oakestra/OU=MQTTS\CN=mqtts"
    else
        echo "DNS Detected"
        openssl req -out server.csr -key server.key -new -addext "subjectAltName = DNS:${SYSTEM_MANAGER_URL}, DNS:mqtts" -subj "/C=DE/ST=Bavaria/L=Munich/O=Oakestra/OU=MQTTS\CN=mqtts"
    fi
fi

openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out server.crt -days 365 -copy_extensions copyall
echo "-------------------------------"
chmod 0644 server.key

# Cluster Manager
echo "Generating a client key"
openssl genrsa -aes256 -out client.key 2048
echo "-------------------------------"
openssl req -out client.csr -key client.key -new -subj "/C=DE/ST=Bavaria/L=Munich/O=Oakestra/OU=Cluster Manager\CN=cluster_manager"
echo "-------------------------------"
openssl x509 -req -in client.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out client.crt -days 365


echo "###############################"
echo "###############################"
echo "Set the client key password as an env:"
echo "export CLUSTER_KEYFILE_PASSWORD=<keyfile password>"
echo "###############################"
echo "###############################"

