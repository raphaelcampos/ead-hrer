commands = {
    'insert': lambda l, values: l.insert(int(values[1]), int(values[2])),
    'print': lambda l, values: print(l),
    'remove': lambda l, values: l.remove(int(values[1])),
    'append': lambda l, values: l.append(int(values[1])),
    'reverse': lambda l, values: l.reverse(),
    'pop': lambda l, values: l.pop(),
    'sort': lambda l, values: l.sort(),
}
    
if __name__ == '__main__':
    N = int(input())
    l = []
    # for para ler as linhas da entrada.
    # serão N linhas após a primeira
    for i in range(N):
        # lendo a linha contendo o comando
        command = input()
        
        # divido-a pelos espaços em branco
        values = command.split()

        # uso meu dicionário de comandos
        # para executar o comando selecionado.
        # note que todas as funções lambdas no
        # dicionário possuem a mesma assinatura,
        # eu deixo a cargo da função tratar o values
        # e a lista l.
        commands[values[0]](l, values) 