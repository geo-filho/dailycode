class Program
{
    static void Main()
    {
        List<string> jogadores = new List<string>();
        List<int> pontuacoes = new List<int>();

        Console.WriteLine("Quantos jogadores deseja cadastrar?");
        int quantidade = Convert.ToInt32(Console.ReadLine());

        for (int i = 0; i < quantidade; i++)
        {
            Console.WriteLine("Digite o nome do jogador:");
            string nome = Console.ReadLine();

            Console.WriteLine("Digite a pontuação:");
            int pontos = Convert.ToInt32(Console.ReadLine());

            jogadores.Add(nome);
            pontuacoes.Add(pontos);
        }

        gerar_ranking(jogadores, pontuacoes);
    }

    static void gerar_ranking(List<string> jogadores, List<int> pontuacoes)
    {
        for (int i = 0; i < pontuacoes.Count - 1; i++)
        {
            for (int j = i + 1; j < pontuacoes.Count; j++)
            {
                if (pontuacoes[j] > pontuacoes[i])
                {
                    int tempPontos = pontuacoes[i];
                    pontuacoes[i] = pontuacoes[j];
                    pontuacoes[j] = tempPontos;

                    string tempJogador = jogadores[i];
                    jogadores[i] = jogadores[j];
                    jogadores[j] = tempJogador;
                }
            }
        }

        Console.WriteLine("\n--- Ranking ---");

        int posicao = 1;

        foreach (string jogador in jogadores)
        {
            Console.WriteLine($"{posicao}º - {jogador} | {pontuacoes[posicao - 1]} pontos");
            posicao++;
        }
    }
}