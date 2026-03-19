static void calcularMedia(double materia1, double materia2, double materia3)
{
    double media = (materia1 + materia2 + materia3) / 3;
    if(media >= 7)
    {
        Console.WriteLine($"Você foi aprovado, sua média foi: {media}");
    } else
    {
        Console.WriteLine($"Você foi reprovado, sua média foi: {media}");
    }
}

Console.WriteLine("Digite sua nota em português: ");
double materia1 = Convert.ToDouble(Console.ReadLine());

Console.WriteLine("Digite sua nota em matemática: ");
double materia2 = Convert.ToDouble(Console.ReadLine());

Console.WriteLine("Digite sua nota em biologia: ");
double materia3 = Convert.ToDouble(Console.ReadLine());

calcularMedia(materia1, materia2, materia3);