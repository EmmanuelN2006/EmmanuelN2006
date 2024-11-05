using System;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            bool hola; bool adios; 
            Console.WriteLine("Ingrese un número"); int valor = Convert.ToInt32(Console.ReadLine()); //Si no se pone Convert.ToInt32, el número se leerá como código Ascii decimal

            if (valor <= 0) //Si el valor del número es mayor que 0 será verdadero, sino es falso
            {
                hola = false; adios = false;
            }
            else
            {
                hola = true; adios = true;
            }

            if (hola && adios) //Sin números o igualdades, las dos variables se toman como verdaderas en la condición
            {
                Console.WriteLine("Hola!");
                Console.WriteLine("Adios!");
            }
            else
            {
                Console.WriteLine("No me hables!");
            }
                

        }
    }
}
