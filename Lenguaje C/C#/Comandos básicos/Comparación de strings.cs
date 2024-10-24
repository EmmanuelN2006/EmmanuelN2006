string palabra1 = "hola";
string palabra2 = "mundo";

if (palabra1 == palabra2)
{
    Console.WriteLine("Las palabras son iguales.");
}
else
{
    Console.WriteLine("Las palabras son diferentes.");
}

// Comparación sin importar mayúsculas
if (palabra1.Equals(palabra2, StringComparison.OrdinalIgnoreCase))
{
    Console.WriteLine("Las palabras son iguales (sin mayúsculas/minúsculas).");
}
