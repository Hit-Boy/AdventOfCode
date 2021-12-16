using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Text;

namespace Task4 {
    class Program {
        static void Main(string[] args) {
            int[] nums;
            int[,,] boards;
            ReadFromInput(out nums, out boards);
            MarkBingo(boards, nums);
            for (int i = 0; i < boards.GetLength(0); i++) {
                for (int j = 0; j < 5; j++) {
                    for (int g = 0; g < 5; g++)
                        Console.Write(boards[i, j, g] + "    ");
                    Console.Write('\n');
                }

                Console.Write('\n');

            }

            static void ReadFromInput(out int[] nums, out int[,,] boards) {
                string filePath = @"C:\MyProjects\AdventOfCode\Solution\Task4\Input.txt";

                List<string> lines = new List<string>();
                lines = File.ReadLines(filePath).ToList();

                char[] line1 = lines[0].ToCharArray();
                int numsCount = 0;
                foreach (char sign in line1) {
                    if (sign == ',')
                        numsCount++;
                }

                nums = new int[numsCount + 1];
                string[] stringNums = lines[0].Split(',', numsCount + 1);
                //Console.WriteLine("{0}", string.Join(' ', stringNums));
                for (int i = 0; i < stringNums.Length; i++) {
                    int.TryParse(stringNums[i], out nums[i]);
                }

                int boardCount = 0;
                for (int i = 1; i < lines.Count; i++) {
                    if (lines[i] == "")
                        boardCount++;
                }

                boards = new int[boardCount, 5, 5];

                for (int i = 0; i < boardCount - 1; i++) {
                    for (int j = 0; j < 5; j++) {
                        string[] boardNums = lines[2 + i * 6 + j].Split(' ', 5);
                        for (int g = 0; g < boardNums.Length; g++)
                            int.TryParse(boardNums[g], out boards[i, j, g]);
                    }
                }
                /*
                for (int i = 0; i < boardCount; i++) {
                    for (int j = 0; j < 5; j++) {
                        for (int g = 0; g < 5; g++) 
                            Console.Write(boards[i, j, g] + "    ");
                        Console.Write('\n');
                    }
                    Console.Write('\n');
                }
                */
            }

            static void MarkBingo(int[,,] boards, int[] nums) {
                foreach (int t in nums) {
                    for (int i = 0; i < boards.GetLength(0); i++) {
                        for (int j = 0; j < boards.GetLength(1); j++) {
                            for (int g = 0; g < boards.GetLength(2); g++)
                                if (boards[i, j, g] == t) {
                                    boards[i, j, g] = -1;
                                    if (CheckBoard(boards, i, j, g)) 
                                        CountBoard(boards, i, t);
                                }

                        }
                    }
                }
            }

            static bool CheckBoard(int[,,] boards, int i, int j, int g) {
                int columnSum = 0;
                int lineSum = 0;
                for (int k = 0; k < boards.GetLength(1); k++)
                    columnSum += boards[i, k, g];
                if (columnSum == -5)
                    return true;
                for (int k = 0; k < boards.GetLength(2); k++)
                    lineSum += boards[i, j, k];
                if (lineSum == -5)
                    return true;
                return false;
            }

            static void CountBoard(int[,,] boards, int boardNum, int num) {
                int boardSum = 0;
                for (int j = 0; j < boards.GetLength(1); j++) {
                    for (int g = 0; g < boards.GetLength(2); g++)
                        if (boards[boardNum, j, g] != -1) {
                            boardSum += boards[boardNum, j, g];
                        }
                }
                Console.WriteLine("AAAAAAND THE WINNER IS: {0}", boardSum * num);
                for (int j = 0; j < boards.GetLength(1); j++) {
                    for (int g = 0; g < boards.GetLength(2); g++)
                        boards[boardNum, g, j] = 100;
                }
                
            }
        }
    }
}