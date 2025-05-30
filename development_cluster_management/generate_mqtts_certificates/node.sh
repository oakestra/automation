echo "Make sure the env CA_CRT and CA_KEY are set to the respective paths"
echo "Generating Client key"
openssl genrsa -aes256 -out client.key 2048
echo "-------------------------------"
openssl req -out client.csr -key client.key -new -subj "/C=DE/ST=Bavaria/L=Munich/O=Oakestra/OU=MQTTS/CN=$(ip -o route get to 8.8.8.8 | sed -n 's/.*src \([0-9.]\+\).*/\1/p')"
echo "-------------------------------"
openssl x509 -req -in client.csr -CA ${CA_CRT} -CAkey ${CA_KEY} -CAcreateserial -out client.crt -days 365 -extfile <(printf "extendedKeyUsage=clientAuth\nkeyUsage=digitalSignature,keyEncipherment\nsubjectAltName=IP:$(ip -o route get to 8.8.8.8 | sed -n 's/.*src \([0-9.]\+\).*/\1/p')")
openssl rsa -in client.key -out unencrypt_client.key
sudo cp ${CA_CRT} /etc/ssl/certs/
sudo c_rehash /etc/ssl/certs/