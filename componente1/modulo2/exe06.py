candidatos = [{"id": 1234, "votos": 0}, {"id": 1235, "votos": 00}, {"id": 1236, "votos": 00}]
qtdNulo = 0

while True:
    print("Vote no seu candidato: ")
    voto = int(input("Em qual candidato você deseja votar? (1234, 1235, 1236)"))

    if voto == 1234:
        candidatos[0]["votos"] += 1
    elif voto == 1235:
        candidatos[1]["votos"] += 1
    elif voto == 1236:
        candidatos[2]["votos"] += 1
    else:
        qtdNulo += 1
    
    encerrarVotacao = int(input("Deseja encerrar a votacão: (0 - Não), (1 - Sim)"))
    if encerrarVotacao == 1:
        break

votosVencedor = 0
idCandidatoVencedor = 0
for candidato in candidatos:
    if candidato["votos"] > votosVencedor:
        idCandidatoVencedor = candidato["id"]

print("Chapa vencedora:",idCandidatoVencedor)
print("Dados sobre a votação:", candidatos)
print("Quantidade de votos nulos:", qtdNulo)