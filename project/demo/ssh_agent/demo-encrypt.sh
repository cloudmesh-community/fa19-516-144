source config.sh

echo " "
echo "Encrypting $TEST_FPATH -> $ENC_FPATH"
echo " "
openssl rsautl -encrypt -oaep -pubin -inkey <(ssh-keygen -e -f $PUB_FPATH -m PKCS8) -in $TEST_FPATH -out $ENC_FPATH
