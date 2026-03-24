class Program
{
    static void Main()
    {
        Console.WriteLine("Insira seu salário: ");
        double salario = Convert.ToDouble(Console.ReadLine());

        Console.WriteLine("Insira o valor da casa que você deseja: ");
        double valorCasa = Convert.ToDouble(Console.ReadLine());

        Console.WriteLine("Insira em quantos anos você quer realizar o pagamento");
        double tempo = Convert.ToDouble(Console.ReadLine());

        simularEmprestimo(salario, valorCasa, tempo);
    }

    static void simularEmprestimo(double salario, double valorCasa, double tempo)
    {
        double prestacao = valorCasa / (tempo * 12);
        double porcetagemsalario = salario * 0.3;
        if (prestacao > porcetagemsalario)
        {
            Console.WriteLine($"A prestação da sua casa ficou por {prestacao} \n Portanto não é possível realizar o empréstimo pois a prestação ficou maior que 30% do seu salário que é igual {porcetagemsalario}");
        } else
        {
            Console.WriteLine("Emprestimo aprovado! \n 30% do seu salário é superior ao valor da prestação");
        }
    }
}