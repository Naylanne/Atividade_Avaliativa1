def ler_jogadores(n):
    jogadores = []
    for _ in range(n):
        nome, h = input().split()
        jogadores.append([nome, int(h)])
    return jogadores


def habilidade(jogador):
    return jogador[1]

def main():
    N, T = map(int, input().split())
    jogadores = ler_jogadores(N)
    jogadores.sort(key=habilidade, reverse=True)
    
    times = [[] for _ in range(T)]
    for i, jogador in enumerate(jogadores):
        times[i % T].append(jogador[0])
    
    for i, time in enumerate(times, start=1):
        print(f"Time {i}")
        for nome in sorted(time):
            print(nome)
        print()

main()