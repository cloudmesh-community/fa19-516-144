source config.sh 

echo " "
echo "Generating key at $PRV_FPATH"
echo "Key password: $KEY_PWD"
echo " "
ssh-keygen -t rsa -b 2048 -m pem -N $KEY_PWD -f $PRV_FPATH
