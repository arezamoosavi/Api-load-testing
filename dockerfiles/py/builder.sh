#!/bin/bash
#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset

echo "No task assigned!"

exec "$@"