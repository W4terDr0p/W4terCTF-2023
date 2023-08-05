#!/bin/sh
echo 'Input your ELF file (base64 encoded):'
read input
echo $input | base64 -d > ./elf
./elf_parser -S ./elf
exit
