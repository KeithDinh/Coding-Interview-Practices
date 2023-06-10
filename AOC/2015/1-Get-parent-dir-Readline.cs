using System.IO;
/**
 * TODO: fetch input from URL using token or pull AOC session from browser cookies
 */


// This will get the current WORKING directory (i.e. \bin\Debug)
string workingDirectory = Environment.CurrentDirectory;
// or: Directory.GetCurrentDirectory() gives the same result

// This will get the current PROJECT bin directory (ie ../bin/)
string projectDirectory = Directory.GetParent(workingDirectory).Parent.FullName;

// This will get the current PROJECT directory
string projectDirectory2 = Directory.GetParent(workingDirectory).Parent.Parent.FullName;

string filePath = $"{projectDirectory2}\\input"; // Specify the file name or path
try
{
    string input = "";
    // Open the text file using a StreamReader
    using (StreamReader sr = new StreamReader(filePath))
    {
        string line;

        // Read and display lines from the file until the end is reached
        while ((line = sr.ReadLine()) != null)
        {
            input += line;
        }
    }

    // Part 1
    int up = input.ToCharArray().Count(c => c == '(');
    int down = input.ToCharArray().Count(c => c == ')');

    Console.WriteLine($"Part 1: {up - down}");

    // Part 2
    int step = 0;
    char[] chars = input.ToCharArray();
    for(int i=0; i<chars.Length; i++)
    {
        step += (chars[i] == '(') ? 1 : -1;
        if (step < 0) {
            Console.WriteLine($"Part 2: {i+1}");
            break; 
        }
    }
    
}
catch (Exception e)
{
    // Handle any exceptions that occur during file reading
    Console.WriteLine("An error occurred while reading the file: " + e.Message);
}
