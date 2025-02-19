#!/bin/bash

# Navega para o diretório onde os arquivos fonte estão
cd src

# Compila todos os arquivos Java dentro de src
javac -d ../bin *.java

# Executa a classe Main (considerando que você está usando pacotes)
java -cp ../bin Main