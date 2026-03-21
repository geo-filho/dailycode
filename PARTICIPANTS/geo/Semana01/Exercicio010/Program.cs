static void main()
{
    Console.WriteLine("Digite o primeiro número: ");
    double num1 = Convert.ToDouble(Console.ReadLine());

    Console.WriteLine("Digite o segundo número: ");
    double num2 = Convert.ToDouble(Console.ReadLine());

    Console.WriteLine("Digite o terceiro número: ");
    double num3 = Convert.ToDouble(Console.ReadLine());

    verificarNumeros(num1, num2, num3);
}

static void verificarNumeros(double num1, double num2, double num3)
{
    double maior = Math.Max(num1, Math.Max(num2, num3));
    double menor = Math.Min(num1, Math.Min(num2, num3));

    Console.WriteLine($"O maior número é: {maior}");
    Console.WriteLine($"O menor número é: {menor}");
}

main();