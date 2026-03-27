class Progam
{
    static void Main()
    {
        Console.WriteLine("Digite uma palavra ou frase para inverter: ");
        string texto = Console.ReadLine();

        string resultado = inverter_texto(texto);

        Console.WriteLine($"Texto invertido: {resultado}");
    }

    static string inverter_texto(string texto)
    {
        string invertido = "";
        int i = texto.Length - 1;

        while (i >= 0)
        {
            invertido = invertido + texto[i];
            i = i - 1;
        }

        return invertido;
    }
}