source config.sh

echo " "
echo "Adding $PRV_FPATH to ssh-agent"
echo "Key Password is: $KEY_PWD"
echo " "
ssh-add $PRV_FPATH
