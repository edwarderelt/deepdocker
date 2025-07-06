#!/bin/bash
set -e

echo "Starting services..."

# Test if health server works standalone
echo "Testing health server..."
python3 /app/health_server.py &
HEALTH_PID=$!
sleep 2

# Test health endpoint
if curl -f http://localhost:8081/health; then
    echo "Health server is working!"
else
    echo "Health server failed to start"
    kill $HEALTH_PID
    exit 1
fi

# Kill test server
kill $HEALTH_PID

# Now start everything with supervisor
echo "Starting all services with supervisor..."
exec /usr/bin/supervisord -c /app/supervisord.conf