rm registros.log
echo "Deletando versões anteriores." >> registros.log
rm -rf \local_lib
echo "Realizando instalação do path.py." >> registros.log
python3 -m pip install  git+https://github.com/jaraco/path.git --target=local_lib 
