#!/bin/bash
# Set an array
IP_ADDRESSES=(192.168.1.1 192.168.1.2 192.168.1.3)
# Print all elements in the array
echo "${IP_ADDRESSES[*]}"
# Print only the first element in the array
echo "${IP_ADDRESSES[0]}"

# Deleting an array

unset IP_ADDRESSES[1]
echo "${IP_ADDRESSES[0]}"
