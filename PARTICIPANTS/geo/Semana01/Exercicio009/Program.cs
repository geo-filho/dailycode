static void main()
{    
Console.WriteLine("Digite o valor do seu salario: ");
double salario = Convert.ToDouble(Console.ReadLine());

Console.WriteLine("Digite a porcetagem de aumento ou descrescimo: ");
double porcetagem = Convert.ToDouble(Console.ReadLine());

Console.WriteLine("Digite 1 para aumento OU 2 para descrescimo: ");
string decisao = Console.ReadLine();

calculoSalario(salario, porcetagem, decisao);
}

static void calculoSalario(double salario, double porcetagem, string decisao)
{
    double porcetagemCalculada = porcetagem / 100;
    if (decisao == "1")
    {
        double salarioAumento = (salario*porcetagemCalculada) + salario;
        Console.WriteLine($"Seu salário reajustado é igual {salarioAumento}");
    } else if (decisao == "2")
    {
        double salarioDescrescimo = salario - (salario*porcetagemCalculada);
        Console.WriteLine($"Seu salário reajustado é igual {salarioDescrescimo}");
    } else
    {
        Console.WriteLine("Digite um número válido");
    }

}

main ();