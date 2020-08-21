using System;

namespace app
{
    class Program
    {
        static void Main(string[] args)
        {
            // masodfoku in c#

            //      -b +- sqrt(b^2 - 4*a*c)
            //      -----------------------
            //                2*a


            // getting input for a, b, c and converting it to a int value
            int a;
                Console.WriteLine("Enter a: ");
                a = int.Parse(Console.ReadLine());
            int b;
                Console.WriteLine("Enter b: ");
                b = int.Parse(Console.ReadLine());
            int c;
                Console.WriteLine("Enter c: ");
                c = int.Parse(Console.ReadLine());

            // declaring variables to look cool
            int minusB = -1 * b;
            int denominator = 2 * a;
            // calculating the value of the discriminant
            int D = (b * b) - (4 * a * c);

            if (a != 0) // a cannot be 0 cuz we will divide by it
            {

                if (D > 0)
                {
                    Console.WriteLine("D is  greater than 0 " + "(" + D + ")");
                    float plusCounter = (int)(minusB + Math.Sqrt(D));
                    float minusCounter = (int)(minusB - Math.Sqrt(D));
                    float x1 = plusCounter / denominator; // value of the first x
                    float x2 = minusCounter / denominator; // value of the second x
                    Console.WriteLine("x1 = " + x1 + " (" + plusCounter + "/" + denominator + ")");
                    Console.WriteLine("x2 = " + x2 + " (" + minusCounter + "/" + denominator + ")");
                } 
                else if(D == 0) 
                {
                    Console.WriteLine("D is equal to 0");
                    float counter = (int)(minusB + Math.Sqrt(D));
                    float x = counter / denominator; // only one x cuz D is 0
                    Console.WriteLine("x = " + x + " (" + counter + "/" + denominator + ")");
                }
                else
                {
                    Console.WriteLine("D is less than 0." + " (" + D + ")");
                }
            } 
            else
            {
                Console.WriteLine("a can't be 0");
            }
        }
    }
}
