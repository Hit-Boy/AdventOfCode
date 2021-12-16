using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.IO;
using System.Linq;
using System.Text;

namespace Task2
{
    class Program
    {
        static void Main(string[] args) {
            string filePath = @"C:\MyProjects\AdventOfCode\Solution\Task2\Input.txt";

            List<string> lines= new List<string>();
            lines = File.ReadLines(filePath).ToList();

            int position = 0;
            int depth = 0;
            int aim = 0;
            

            foreach (string line in lines) {
                int num = 0;
                string[] split = line.Split(' ', 2);
                int.TryParse(split[1], out num);
                if (split[0] == "forward") {
                    position += num;
                    depth += aim * num;
                }
                else if (split[0] == "down")
                    aim += num;
                else aim -= num;
                    
                    
                Console.WriteLine(line);
            }
            Console.WriteLine("position {0} depth {1}", position, depth);
            Console.WriteLine(position * depth);
        }
    }
}