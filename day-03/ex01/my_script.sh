log=/ex01/local_lib/registros.log
echo "Verificando se o módulo já foi previamente instalado." >> registros.log

rmdir \local_lib
mkdir \local_lib
chmod +rwx \local_lib
python3   -m pip install --target=local_lib path.py