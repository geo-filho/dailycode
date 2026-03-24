class Program
{
    static void Main()
    {
        Console.WriteLine("Insira o valor do depósito: ");
        double deposito = Convert.ToDouble(Console.ReadLine());

        Console.WriteLine("Insira a porcetagem de juros ao mês: ");
        double porcetagemJuros = Convert.ToDouble(Console.ReadLine());

        Console.WriteLine("Insira em quantos meses você quer simular:");
        double tempoMeses = Convert.ToDouble(Console.ReadLine());

        simularInvestimento(deposito, porcetagemJuros, tempoMeses);
    }

    static void simularInvestimento(double deposito, double porcetagemJuros, double tempoMeses)
    {
        for(int i = 0; i <= tempoMeses; i++)
        {
            double valorJuros = deposito * (porcetagemJuros/100); 
            deposito = deposito + valorJuros;
            Console.WriteLine($"O valor no mês {i} foi igual a {deposito:f2}");
        }
    }
}