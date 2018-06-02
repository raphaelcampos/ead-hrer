if __name__ == '__main__':
    registros = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        registros.append([name, score])
    
    # ordeno primeiro pelo nome em order alfabética    
    registros.sort(key=lambda x: x[0])
    # ordeno novamente, porém pelo score
    # como o algoritmo do sort do python é hibrido entre
    # o mergesort e o insertion sort (timsort) ele mantém
    # a ordem original em caso de empate, portanto,
    # mantendo a ordem alfabético para alunos com mesmo score.
    registros.sort(key=lambda x: x[1])

    # como número de registro é sempre maior que 2
    # posso fazer isso sem problemas
    menor_score = registros[0][1]
    
    j = 0
    for i in range(1, len(registros)):
        # como está ordenado por score, enquanto for o menor score
        # não será feito nada, apenas quando chegarmos no segundo menor
        # score o expressão será verdadeira.
        # nesse ponto a variável menor score vai receber o valor do segundo
        # menor score e j será incrementado. Desse modo, a expressão nunca mais
        # será verdadeira.
        if not (registros[i][1] == menor_score) and j == 0:
            j += 1
            menor_score = registros[i][1]
        
        # essa expressão só será verdadeira quando o segundo menor score for
        # encontrado. Lembre-se que enunciado fala que sempre haverá o segundo
        # menor score, por isso que o algoritmo funciona.
        if registros[i][1] == menor_score and j == 1:
            print(registros[i][0])