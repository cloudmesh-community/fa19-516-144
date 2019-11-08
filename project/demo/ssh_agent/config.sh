#!/usr/bin/bash
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
