class Progam
{
    static void Main()
    {
        Console.WriteLine("Digite sua nova senha: ");
        string ?senha = Console.ReadLine();

        validarSenha(senha);
    }

    static void validarSenha(string senha)
    {

        bool temNumero = false;
        bool temMaiuscula = false;
        if (senha.Length < 8)
        {
            Console.WriteLine("Sua senha deve conter no mínimo 8 digitos...");
        }
        else
        {
            for(int i=0; i < senha.Length; i++)
            {
                char letra = senha[i];
                if (char.IsUpper(letra))
                {
                    temMaiuscula = true;
                }

                if (char.IsNumber(letra))
                {
                    temNumero = true;
                }            
            }
            if (temMaiuscula && temNumero)
            {
                Console.WriteLine("Sua senha foi validada");
            }
            else
            {
                Console.WriteLine("Sua senha deve conter 1 número e 1 letra maiuscula");
            }
        }
    }
}