class Progam
{
    static void Main()
    {
        Console.WriteLine("Insira um número para verificar se é primo: ");
        double numero = Convert.ToDouble(Console.ReadLine());

        Console.WriteLine(verificarNumero(numero));
    }

    static string verificarNumero(double numero)
    {
        int i = 2;
        if (numero <= 1 )
        {
            return "O número não é primo";
        }
        else
        {
            while (i < numero)
            {
                if (numero % i == 0)
                {
                    i++;
                    return "O número não é primo";
                }
            }
             return "O número é primo";
        }
    }
}