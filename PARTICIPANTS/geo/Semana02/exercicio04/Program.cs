class Progam
{
    static void Main()
    {
        Console.WriteLine("Digite um valor para a contagem: ");
        int numeroContagem = Convert.ToInt32(Console.ReadLine());

        iniciarCronometro(numeroContagem);
    }

    static void iniciarCronometro(int numeroContagem)
    {
        int contador = numeroContagem;
        while (contador > 0)
        {
            contador = contador - 1;
            Console.WriteLine(contador);
        }
    }
}