    using System;
    using System.Collections.Generic;
    using System.ComponentModel;
    using System.Globalization;
    using System.IO;
    using System.Linq;
    using System.Text;

    namespace Task3
    {
        class Program
        {
            static void Main(string[] args) {
                string filePath = @"C:\MyProjects\AdventOfCode\Solution\Task3\Input.txt";

                List<string> lines = new List<string>();
                lines = File.ReadLines(filePath).ToList();
            List<string> tmp = lines;

            int[] nums = new int[12];
            int[] epsilonRate = {0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1};
            int[] gammaRate = {1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0};
            
            //001000111101
            //101101010110
            
            for(int i = 0; i < nums.Length; i++) {
                int num = 0;
                for (int j = 0; j < tmp.Count; j++) {
                    char[] charLine = tmp[j].ToArray();
                    if (charLine[i] == '1') {
                        num++;
                    }
                    else {
                        num--;
                    }
                }
                char targetNum = num >= 0 ? '0' : '1';
               // Console.WriteLine(targetNum + "eeeeeeeeeeeeee");
                
                for (int j = 0; j < tmp.Count; j++) {
                    char[] charLine = tmp[j].ToArray();
                   // Console.WriteLine("\n{0}, {1}", j, i);
                   // Console.WriteLine(charLine[i] + " " + targetNum);
                    
                    if (charLine[i] != targetNum) { 
                        //Console.WriteLine("removed");
                        tmp.RemoveAt(j);
                        if (j > 0)
                            j--;
                    }
                    
                }
                Console.WriteLine("[{0}]", string.Join(", ", tmp));
            }

            Console.WriteLine("[{0}]", string.Join(", ", nums));

            //MakeBinaries(nums, out gammaRate, out epsilonRate);
            //Console.WriteLine("[{0}]", string.Join(", ", gammaRate));
            //Console.WriteLine("[{0}]", string.Join(", ", epsilonRate));
            float num1 = MakeDecimal(gammaRate);
            float num2 = MakeDecimal(epsilonRate);
            Console.WriteLine("{0} * {1} = {2}", num1, num2, num1 * num2);
        }

        private static void MakeBinaries(int[] nums, out int[] gammaRate, out int[] epsilonRate) {
            int[] binaryGamma = new int[nums.Length];
            int[] binaryEpsilon = new int[nums.Length];
            for (int i = 0; i < nums.Length; i++) {
                if (nums[i] > 0) {
                    binaryGamma[i] = 1;
                    binaryEpsilon[i] = 0;
                }
                else {
                    binaryGamma[i] = 0;
                    binaryEpsilon[i] = 1;
                }
            }

            gammaRate = binaryGamma;
            epsilonRate = binaryEpsilon;
        }

        private static float MakeDecimal(int[] num) {
            float returnNum = 0;
            for (int i = 0; i < num.Length; i++) {
                returnNum +=  num[i] * MathF.Pow(2, num.Length - i - 1);
                Console.WriteLine(num.Length - i - 1 + " " + returnNum);
            }
            return returnNum;
        }
    }
}