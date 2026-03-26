class Progam
{
    static void Main()
    {
        Console.WriteLine("Sequência de Fibonacci");
        Console.WriteLine("Insira um número para ver a sequência até a posição: ");
        int numero = Convert.ToInt32(Console.ReadLine());

        List<int> resultado = verificarFibonacci(numero);
        foreach (int n in resultado)
        {
            Console.WriteLine(n);
        }
    }

    static List<int> verificarFibonacci(int numero)
    {
        List<int> sequencia = new List<int>();
        
        
        int i = 0;
        int a = 0;
        int b = 1;

        sequencia.Add(a);
        sequencia.Add(b);

        int proximo = 0;

        while (i < numero)
        {
            proximo = a + b;
            sequencia.Add(proximo);
            a = b;
            b = proximo;
            i++;
        }

        return sequencia;
    }
}