static void converterMilimetro(double metro)
{
    double valorConvertido = metro / 1000;
    Console.WriteLine($"{metro} convertido em milimetros é igual a: {valorConvertido}"); 
}

Console.WriteLine("Digite quando você quer converter: "); 
double metro = Convert.ToDouble(Console.ReadLine());
converterMilimetro(metro);
