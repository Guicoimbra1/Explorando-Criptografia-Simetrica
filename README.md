!! É NECESSÁRIO TER O PACOTE "cryptography" INSTALADO, PARA ISSO EXECUTE O COMANDO "pip install cryptography" OU "python -m pip install cryptography" NO SEU TEMINAL DE COMANDO!!

Este é um pequeno projeto explorando criptografia simétrica em Python

É muito simples usar, ao iniciar o programa, caso você não possua uma chave de criptografia use a opção "Gerar Chave", uma chave irá aparecer que pode ser copiada.
O programa também criará um arquivo "chave.key" na mesma pasta do programa (que pode ser aberto usando o bloco de notas) contendo a chave recém gerada, mas cuidado, se outra chave for gerada
a chave existente no arquivo será subistituida pela nova.

Na criptografia simétrica, um texto ou arquivo só pode ser descriptografado usando a mesma chave usada para criptografá-lo, logo sugiro guardar bem a chave usada para criptografar.

Se desejar criptografar ou descriptografar um texto, simplesmente digite-o quando for requerido, caso deseje criptografar ou descriptografar um arquivo, digite o nome do arquivo exatamente igual ao do arquivo
contendo a sua extensão (ex: arquivo.txt ou audio.mp3)

importante lembrar que o arquivo deve estar presente na mesma pasta que o programa, caso alguma dessas orientações não for seguida o arquivo não será criptografado.

Após inserir o texto ou nome de arquivo aperte ENTER, insira a chave quando for pedida, aperte ENTER e pronto.
As únicas chaves que funcionam neste programa são as suportadas pelo fernet (base64, 32 bytes) 

Funciona com quase todo tipo de arquivos texto, áudio, vídeo, imagens, etc...

Incluí alguns arquivos para testes.
Divirta-se ;)


