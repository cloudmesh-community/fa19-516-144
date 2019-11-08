source config.sh

echo " " 
echo "Decrypting $ENC_FPATH -> $DEC_FPATH"
echo "Key password: $KEY_PWD"
echo " "
openssl rsautl -decrypt -oaep -inkey $PRV_FPATH -in $ENC_FPATH -out $DEC_FPATH

echo " "
echo "About to compare $TEST_FPATH and $DEC_FPATH" 
echo "Sucess if bytes are identical"
sleep 1s
cmp --silent $TEST_FPATH $DEC_FPATH && echo "SUCCESS" || "FAILURE"
