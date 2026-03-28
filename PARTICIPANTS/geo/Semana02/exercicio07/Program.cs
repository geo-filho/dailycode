class Program
{
    static void Main()
    {
        List<string> produtos = new List<string>();
        int opcao = 0;

        while (opcao != 5)
        {
            Console.WriteLine("\n--- MENU ---");
            Console.WriteLine("1 - Adicionar produto");
            Console.WriteLine("2 - Remover produto");
            Console.WriteLine("3 - Listar produtos");
            Console.WriteLine("4 - Buscar produto");
            Console.WriteLine("5 - Sair");

            opcao = Convert.ToInt32(Console.ReadLine());

            if (opcao == 1)
            {
                Console.WriteLine("Digite o nome do produto:");
                string nome = Console.ReadLine();
                adicionarProduto(produtos, nome);
            }

            if (opcao == 2)
            {
                Console.WriteLine("Digite o produto para remover:");
                string nome = Console.ReadLine();
                removerProduto(produtos, nome);
            }

            if (opcao == 3)
            {
                listarProdutos(produtos);
            }

            if (opcao == 4)
            {
                Console.WriteLine("Digite o produto para buscar:");
                string nome = Console.ReadLine();
                buscarProduto(produtos, nome);
            }
        }
    }

    static void adicionarProduto(List<string> produtos, string nome)
    {
        produtos.Add(nome);
        Console.WriteLine("Produto adicionado.");
    }

    static void removerProduto(List<string> produtos, string nome)
    {
        if (produtos.Contains(nome))
        {
            produtos.Remove(nome);
            Console.WriteLine("Produto removido.");
        }
        else
        {
            Console.WriteLine("Produto não encontrado.");
        }
    }

    static void listarProdutos(List<string> produtos)
    {
        Console.WriteLine("\nProdutos em estoque:");

        foreach (string produto in produtos)
        {
            Console.WriteLine(produto);
        }
    }

    static void buscarProduto(List<string> produtos, string nome)
    {
        if (produtos.Contains(nome))
        {
            Console.WriteLine("Produto existe no estoque.");
        }
        else
        {
            Console.WriteLine("Produto não encontrado.");
        }
    }
}