class Progam
{
    static void Main()
    {
        Console.WriteLine("Coloque o valor da compra para verificar o desconto: ");
        int valorCompra = Convert.ToInt32(Console.ReadLine());

        Console.WriteLine(verificarDesconto(valorCompra));
    }

    static string verificarDesconto(int valorCompra)
    {
        if (valorCompra  <= 100)
        {
            return $"Para compras até 100 reais não há desconto \n Todal da compra: {valorCompra}";
        } else if (valorCompra > 100 && valorCompra < 501) {
            return $"Para compras acima de R$100 até R$500 você recebe 10% \n Todal da compra: {valorCompra - (valorCompra * 0.1)}";
        } else
        {
            return $"Para compras acima de R$500 você recebe 20% \n Todal da compra: {valorCompra - (valorCompra * 0.2)}";
        }
    }
}