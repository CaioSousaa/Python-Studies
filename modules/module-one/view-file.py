# with garante que o arquivo seja iniciado e finalizado ao fim da atividade.
with open("C:/Users/caiod/OneDrive/dev/Phyton/aulas/modules/module-one/file.txt", "r") as file: 
    doc = file.read() # mostra todo o conteúdo do arquivo
print(doc)

# maneira de ler todo o arquivo mas removendo os \n e os espaços não utilizados 
with open("C:/Users/caiod/OneDrive/dev/Phyton/aulas/modules/module-one/file.txt", "r") as file_full_readline: 
    doc_readline = file_full_readline.readline() # mostra apenas a primeira linha do arquivo

    while doc_readline: 
        print(doc_readline.strip()) # .strip() remove espaços em brancos e quebras de linhas extras
        doc_readline = file_full_readline.readline()


with open("C:/Users/caiod/OneDrive/dev/Phyton/aulas/modules/module-one/file.txt", "r") as file_readline: 
    doc_readline = file_readline.readline() # mostra apenas a primeira linha do arquivo
print(doc_readline)


with open("C:/Users/caiod/OneDrive/dev/Phyton/aulas/modules/module-one/file.txt", "r") as file_readlines: 
    doc_readlines = file_readlines.readlines() # mostra todo o conteúdo do arquivo como se estivesse em um array.
print(doc_readlines)

#mostrando uma linha especifica 
with open("C:/Users/caiod/OneDrive/dev/Phyton/aulas/modules/module-one/file.txt", "r") as f: 
    doc_f = f.readlines()

    # uso da função .len() para dizer o tamanho do objeto, pode ser quantidade de valores ou de caracteres
    if len(doc_f) >= 3: # verificando se o arquivo possui mais de 5 linhas
        print(doc_f[2])
    else:
        print("pagina não existente!")
