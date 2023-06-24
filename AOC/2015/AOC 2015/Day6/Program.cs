using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Globalization;
/**
 * TODO: fetch input from URL using token or pull AOC session from browser cookies
 */
int[,] grid = new int[1000, 1000];

try
{
    // Open the text file using a StreamReader
    using (StreamReader sr = new StreamReader(getFilePath()))
    {
        string line, action;
        int[,] points = new int[2, 2];

        // Read and display lines from the file until the end is reached
        while ((line = sr.ReadLine()) != null)
        {
            parseCommand(line, out action, ref points);
            if (action != null && action != "")
                processCommandPart2(action, points);
        }
    }

    // Part 1
    //int count = 0;
    //for (int i = 0; i < grid.GetLength(0); i++)
    //{
    //    for (int j = 0; j < grid.GetLength(1); j++)
    //    {
    //        count = (grid[i, j] == 1) ? count + 1 : count;
    //    }
    //}
    //Console.WriteLine($"Part 1: {count}");
    // Part 2
    int brightnessLevel = 0;
    for (int i = 0; i < grid.GetLength(0); i++)
    {
        for (int j = 0; j < grid.GetLength(1); j++)
        {
            brightnessLevel += grid[i, j];
        }
    }
    Console.WriteLine($"Part 2: {brightnessLevel}");
}
catch (Exception e)
{
    // Handle any exceptions that occur during file reading
    Console.WriteLine("An error occurred while reading the file: " + e.Message);
}
string getFilePath()
{
    // This will get the current WORKING directory (i.e. \bin\Debug)
    string workingDirectory = Environment.CurrentDirectory;
    // or: Directory.GetCurrentDirectory() gives the same result

    // This will get the current PROJECT bin directory (ie ../bin/)
    string projectDirectory = Directory.GetParent(workingDirectory).Parent.FullName;

    // This will get the current PROJECT directory
    string projectDirectory2 = Directory.GetParent(workingDirectory).Parent.Parent.FullName;

    string filePath = $"{projectDirectory2}\\input"; // Specify the file name or path

    return filePath;
}
void parseCommand(string command, out string action, ref int[,] points)
{
    if (command.Length > 0)
    {
        string[] parsed = command.Split(' ');
        string[] point1Parsed, point2Parsed;
        if (parsed[0] == "turn")
        {
            action = parsed[1];
            point1Parsed = parsed[2].Split(',');
            point2Parsed = parsed.Last().Split(",");
        }
        else
        {
            action = parsed[0];
            point1Parsed = parsed[1].Split(',');
            point2Parsed = parsed.Last().Split(",");
        }

        points[0, 0] = int.Parse(point1Parsed[0], NumberStyles.AllowThousands);
        points[0, 1] = int.Parse(point1Parsed[1], NumberStyles.AllowThousands);
        points[1, 0] = int.Parse(point2Parsed[0], NumberStyles.AllowThousands);
        points[1, 1] = int.Parse(point2Parsed[1], NumberStyles.AllowThousands);
    }
    else
        action = null;
}
void processCommandPart1(string command, int[,] points)
{
    if (command == "") return;

    int value = -1;
    if (command == "on")
    {
        value = 1;
    }
    else if (command == "off")
    {
        value = 0;
    }
    else if (command == "toggle")
    {
        value = 2;
    }

    for (int i = points[0, 0]; i <= points[1, 0]; i++)
    {
        for (int j = points[0, 1]; j <= points[1, 1]; j++)
        {
            grid[i, j] = value != 2 ? value : grid[i, j] ^ 1;
        }
    }
}
void processCommandPart2(string command, int[,] points)
{
    if (command == "") return;

    int value = -1;
    if (command == "on")
    {
        value = 1;
    }
    else if (command == "off")
    {
        value = -1;
    }
    else if (command == "toggle")
    {
        value = 2;
    }

    for (int i = points[0, 0]; i <= points[1, 0]; i++)
    {
        for (int j = points[0, 1]; j <= points[1, 1]; j++)
        {
            grid[i, j] = grid[i, j] + value < 0 ? 0 : grid[i, j] + value;
        }
    }
}