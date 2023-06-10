using System.IO;
/**
 * TODO: fetch input from URL using token or pull AOC session from browser cookies
 */

try
{
    string input = "";
    // Open the text file using a StreamReader
    using (StreamReader sr = new StreamReader(getFilePath()))
    {
        string line;

        // Read and display lines from the file until the end is reached
        while ((line = sr.ReadLine()) != null)
        {
            input += line;
        }
    }
    // Part 1
    //Dictionary<int, HashSet<int>> houses = new Dictionary<int, HashSet<int>>();
    //houses.Add(0, new HashSet<int>() { 0 });

    //int x = 0, y = 0;
    //foreach(char c in input.ToCharArray())
    //{
    //    setCoordinates(ref x, ref y, c);
    //    if (!houses.ContainsKey(x))
    //    {
    //        houses.Add(x, new HashSet<int>());
    //    }
    //    houses[x].Add(y);
    //}

    //int totalHouses = 0;
    //foreach(HashSet<int> value in houses.Values)
    //{
    //    totalHouses += value.Count;
    //}
    //Console.WriteLine($"Part 1: {totalHouses}");


    // Part 2
    Dictionary<int, HashSet<int>> houses = new Dictionary<int, HashSet<int>>();
    houses.Add(0, new HashSet<int>() { 0 });

    int x = 0, y = 0, x1 = 0, y1 = 0, turn = 0;
    foreach (char c in input.ToCharArray())
    {
        if (turn == 0)
        {
            setCoordinates(ref x, ref y, c);
            turn = 1;
            if (!houses.ContainsKey(x))
            {
                houses.Add(x, new HashSet<int>());
            }
            houses[x].Add(y);
        }
        else
        {
            setCoordinates(ref x1, ref y1, c);
            turn = 0;
            if (!houses.ContainsKey(x1))
            {
                houses.Add(x1, new HashSet<int>());
            }
            houses[x1].Add(y1);
        }

        
    }

    int totalHouses = 0;
    foreach (HashSet<int> value in houses.Values)
    {
        totalHouses += value.Count;
    }
    Console.WriteLine($"Part 1: {totalHouses}");
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
void setCoordinates(ref int x, ref int y, char direction)
{
    if (direction == '>')
    {
        x += 1;
    } else if (direction == '<')
    {
        x -= 1;
    } else if (direction == '^')
    {
        y += 1;
    } else if (direction == 'v')
    {
        y -= 1;
    }
}
