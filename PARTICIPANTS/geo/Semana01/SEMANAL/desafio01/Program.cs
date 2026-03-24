class Program
{
    static void Main()
    {
        bool autenticado = false; //declaração fora da função para garantir escopo
        for (int i = 0; i < 3; i++)
        {
            Console.WriteLine("Login: ");
            string? login = Console.ReadLine();

            Console.WriteLine("Senha: ");
            string? senha = Console.ReadLine();

            autenticado = loginAuthentication(login, senha);

            if (autenticado == true)
            {
                break;
            }
        }

        if (!autenticado)
        {
            Console.WriteLine("Número de tentativas excedido.");
        }
    
    }

    static bool loginAuthentication(string login, string senha)
    {
        if(login == "admin" && senha == "123")
        {
            Console.WriteLine("Logado com sucesso!");
            return true;
        } else
        {
            Console.WriteLine("Insira dados válidos");
            return false;
        }
    }
}