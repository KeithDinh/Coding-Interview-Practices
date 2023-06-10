using System.IO;
/**
 * TODO: fetch input from URL using token or pull AOC session from browser cookies
 */

try
{
    int totalSqFt = 0;
    int totalRibbon = 0;
    // Open the text file using a StreamReader
    using (StreamReader sr = new StreamReader(getFilePath()))
    {
        string line;

        // Read and display lines from the file until the end is reached
        while ((line = sr.ReadLine()) != null)
        {
            totalSqFt += getTotalArea(line);
            totalRibbon += getTotalRibbon(line);
        }
    }
    // Part 1
    Console.WriteLine($"Part 1: {totalSqFt}");
    // Part 2
    Console.WriteLine($"Part 2: {totalRibbon}");
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
int getTotalArea(string line)
{
    int[] dimensions = line.Split('x').Select(i => int.Parse(i)).ToArray();
    Array.Sort(dimensions);


    return 2 * (dimensions[0] * dimensions[1] +
        dimensions[1] * dimensions[2] +
        dimensions[2] * dimensions[0]) + dimensions[0] * dimensions[1];
}
int getTotalRibbon(string line)
{
    int[] dimensions = line.Split('x').Select(i => int.Parse(i)).ToArray();
    Array.Sort(dimensions);


    return 2 * (dimensions[0] + dimensions[1]) +
        dimensions[0] * dimensions[1] * dimensions[2];
}