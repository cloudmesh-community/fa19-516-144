#!/bin/bash
# Just for PoC test to show ssh-agent cannot be used with decryption
# If encryption is used do NOT use ssh-keygen (it uses weak padding)
# ssh-keygen is used for eas of adding with ssh-add 

# Test Directory
TEST_DIR="$HOME/.cloudmesh/test"
TEST_DATA="Cloudmesh for the win!!!"

# Private Public Key
KEY_PWD="cmstest"
KEY_NAME="cms-key.pem"
PRV_FPATH="$TEST_DIR/$KEY_NAME"
PUB_FPATH="$PRV_FPATH.pub"

# Test File
TEST_NAME="data"
TEST_FPATH="$TEST_DIR/$TEST_NAME"
ENC_FPATH="$TEST_FPATH.enc"
DEC_FPATH="$TEST_FPATH.dec"
DEC_AGENT_FPATH="$TEST_FPATH-agent.dec"

# Ensure Test Dir exists
if [ ! -d "$TEST_DIR" ]; then
  mkdir $TEST_DIR
fi

# Generates Data File
if [ ! -f "TEST_DIR/data" ]; then
  echo $TEST_DATA > $TEST_FPATH
fi

echo " "
echo "Generating key at $PRV_FPATH"
echo "Key password: $KEY_PWD"
echo " "
ssh-keygen -t rsa -b 2048 -m pem -N $KEY_PWD -f $PRV_FPATH

echo " "
echo "Encrypting $TEST_FPATH -> $ENC_FPATH"
echo " "
openssl rsautl -encrypt -oaep -pubin -inkey <(ssh-keygen -e -f $PUB_FPATH -m PKCS8) -in $TEST_FPATH -out $ENC_FPATH

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

echo " "
echo "Adding $PRV_FPATH to ssh-agent"
echo "Key Password is: $KEY_PWD"
echo " "
ssh-add $PRV_FPATH

echo " "
echo "Pausing script for 5 seconds so you have time to read next lines"
echo "If we are prompted for a password we know that even if key is added to
agent it cannot use the private key bytes for decryption"
sleep 5s

# Attempt decryption after key was added to agent
openssl rsautl -decrypt -oaep -inkey $PRV_FPATH -in $ENC_FPATH -out $DEC_AGENT_FPATH

