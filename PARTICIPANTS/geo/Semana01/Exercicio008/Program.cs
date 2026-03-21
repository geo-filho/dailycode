static void main()
{    
Console.WriteLine("Digite a quantidade de dias: ");
double dias = Convert.ToDouble(Console.ReadLine());

Console.WriteLine("Digite a quantidade de horas: ");
double horas = Convert.ToDouble(Console.ReadLine());

Console.WriteLine("Digite a quantidade de minutos: ");
double minutos = Convert.ToDouble(Console.ReadLine());

Console.WriteLine("Digite a quantidade de segundos: ");
double segundos = Convert.ToDouble(Console.ReadLine());

calculoSegundos(dias, horas, minutos, segundos);
}

static void calculoSegundos(double dias, double horas, double minutos, double segundos)
{
    double diasSegundo = dias * 86400;
    double horasSegundo = horas * 3600;
    double minutosSegundo = minutos * 60;

    double totalSegundos = diasSegundo + horasSegundo + minutosSegundo + segundos;
    Console.WriteLine($"{dias} dias em segundo é igual: {diasSegundo} \n {horas} horas em segundo é igual: {horasSegundo} \n {minutos} minutos em segundo é igual: {minutosSegundo} \n O total é igual: {totalSegundos}");
}

main ();