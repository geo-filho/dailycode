static void calcularImposto(double salario)
{
    if (salario > 1200)
    {
        Console.WriteLine($"Você deve pagar imposto, pois seu salário é de: {salario}");
    } else
    {
        Console.WriteLine($"Você nao precisa pagar imposto, pois seu salário é de: {salario}");
    }
}

calcularImposto(1200.50);