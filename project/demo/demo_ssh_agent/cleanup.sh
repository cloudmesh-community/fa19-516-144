source config.sh

# Ensure Test Dir exists
if [ -d "$TEST_DIR" ]; then
  rm -r $TEST_DIR
fi
