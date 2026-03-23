class Program
{
    static void Main()
    {
        string texto = "";
        bool valido = false;

        while (!valido)
        {
            Console.WriteLine("Insira uma palavra ou frase para fazer a contagem de vogais e consoantes:");
            texto = Console.ReadLine();

            valido = true;

            for (int i = 0; i < texto.Length; i++)
            {
                char letra = texto[i];

                if (!char.IsLetter(letra) && letra != ' ')
                {
                    valido = false;
                    break;
                }
            }

            if (!valido)
            {
                Console.WriteLine("Digite apenas letras e espaços!");
            }
        }

        contarVogais(texto);
        contarConsoantes(texto);
    }

    static void contarVogais(string texto)
    {
        int contador = 0;
        string vogais = "";
        texto = texto.ToLower();

        for (int i = 0; i < texto.Length; i++)
        {
            char letra = texto[i];

            if (letra == 'a' || letra == 'e' || letra == 'i' || letra == 'o' || letra == 'u')
            {
                vogais = vogais + " " + letra;
                contador++;
            }
        }

        Console.WriteLine($"Você tem {contador} vogais");
        Console.WriteLine($"Suas vogais são:{vogais}");
    }

    static void contarConsoantes(string texto)
    {
        int contador = 0;
        string consoantes = "";
        texto = texto.ToLower();

        for (int i = 0; i < texto.Length; i++)
        {
            char letra = texto[i];

            if (char.IsLetter(letra) &&
                letra != 'a' && letra != 'e' && letra != 'i' && letra != 'o' && letra != 'u')
            {
                consoantes = consoantes + " " + letra;
                contador++;
            }
        }

        Console.WriteLine($"Você tem {contador} consoantes");
        Console.WriteLine($"Suas consoantes são:{consoantes}");
    }
}