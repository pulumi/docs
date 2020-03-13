# Start a heartbeat process to write data to STDOUT even if there is a long
# delay in updates from the Hugo build process. This keeps Travis from assuming our
# jobs have hung. (Ping every min, stop beating after an hour.)
./scripts/emit-heartbeat.sh 60 3600 &
HEARTBEAT_PID=$!
echo "Started hearbeat process on PID ${HEARTBEAT_PID}"

stop_heartbeat() {
    kill -9 ${HEARTBEAT_PID} || echo "Error killing heartbeat process."
}
trap stop_heartbeat EXIT

NODE_ENV=production hugo --minify -v
