#!/bin/bash

if [ -e 'log_file.log']; then
    rm log_file.log
fi

echo "Verificando se o path.py já está instalado." >> log_file.log

if [ -d '/local_lib' ]; then 
    echo "Deletando versões anteriores." >> log_file.log
    rm -rf \local_lib
fi 

echo "Realizando instalação do path.py." >> log_file.log
python3 -m pip install  git+https://github.com/jaraco/path.git --target=local_lib 


if [ $? -eq 0 ]; then
    echo "Instalação bem-sucedida. Executando o programa Python..." >> log_file.log
    python3 "my_program.py"
else
    echo "Erro durante a instalação. Consulte o arquivo log_file.log para obter detalhes." >> log_file.log
fi