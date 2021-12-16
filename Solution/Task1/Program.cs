using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.IO;
using System.Linq;
using System.Text;

namespace Task1
{
    class Program
    {
        static void Main(string[] args) {
            string filePath = @"C:\MyProjects\AdventOfCode\Solution\Task1\Input.txt";

            List<string> lines= new List<string>();
            lines = File.ReadLines(filePath).ToList();

            int prevSum = 0;
            
            int count = -1;

            for(int i = 2; i < lines.Count; i++) {
                int tmp0 = 0;
                int tmp1 = 0;
                int tmp2 = 0;
                int.TryParse(lines[i-2], out tmp0);
                int.TryParse(lines[i-1], out tmp1);
                int.TryParse(lines[i], out tmp2);
                int sum = tmp0 + tmp1 + tmp2;
                Console.WriteLine(sum + " " + prevSum);
                if (prevSum < sum) {
                    count++;
                    Console.WriteLine(count);
                }
                    
                prevSum = sum;
            }
           // Console.WriteLine(count);
           // Console.ReadLine();
        }
    }
}
