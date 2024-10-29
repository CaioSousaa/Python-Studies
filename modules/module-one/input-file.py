# usando o modo de abertura w para escrever no arquivo
# usando dessa forma, acaba sendo ineficaz, pois ele sobrescreve o texto que já existia.
with open("modules/module-one/input-file.txt", "w") as f:
    f.write("esta eh a primeira linha desse arquivo.\n")

#usando a de append, ele adicona uma nova linha
with open("modules/module-one/input-file.txt", "a") as f:
    f.write("uma nova linha adiconada.\n")

# usando a função input para receber texto do teclado.
with open("modules/module-one/input-file.txt", "a") as f:
    ipunt_file = input("digite algo: ")
    f.write(ipunt_file)