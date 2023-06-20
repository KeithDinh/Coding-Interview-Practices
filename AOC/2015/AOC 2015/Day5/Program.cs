using System.IO;
using System.Collections.Generic;
using System.Linq;
/**
 * TODO: fetch input from URL using token or pull AOC session from browser cookies
 */
List<char> vowels = new List<char>() { 'a', 'e', 'o', 'u', 'i' };
List<string> excludes = new List<string>() { "ab", "cd", "pq", "xy" };
try
{
    int niceStringCountPart1 = 0, niceStringCountPart2 = 0;
    // Open the text file using a StreamReader
    using (StreamReader sr = new StreamReader(getFilePath()))
    {
        string line;

        // Read and display lines from the file until the end is reached
        while ((line = sr.ReadLine()) != null)
        {
            if (isNiceStringPart1(line.Trim()))
                niceStringCountPart1++;
            if (isNiceStringPart2(line.Trim()))
                niceStringCountPart2++;
        }
    }

    // Part 1
    Console.WriteLine(niceStringCountPart1);
    // Part 2
    Console.WriteLine(niceStringCountPart2);
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
bool isNiceStringPart1(string s)
{
    if (s.Length == 0) return false;

    int countVowel = 0;
    bool containExcludes = false,
        hasDoubleChar = false;

    for(int i = 0; i < s.Length; i++)
    {
        if (vowels.Contains(s[i])) 
            countVowel++; 

        if(i+1 < s.Length && excludes.Contains(s.Substring(i, 2)))
            containExcludes = true;

        if (i + 1 < s.Length && s[i] == s[i+1])
            hasDoubleChar = true;
    }
    if (countVowel < 3 || containExcludes || !hasDoubleChar) { return false;  }

    return true;
}
bool isNiceStringPart2(string s)
{
    if (s.Length == 0) return false;

    bool hasRightPair = false,
        hasLetterRepeat = false;

    for (int i = 0; i < s.Length; i++)
    {
        try
        {
            if (i + 2 < s.Length && s[i] == s[i + 2])
                hasLetterRepeat = true;
        }
        catch (Exception)
        {
            Console.WriteLine('1');
            throw;
        }

        try
        {
            string rest = (i < s.Length - 3) ? s.Substring(i + 2) : "";

            if (i+1 < s.Length && 
                rest.IndexOf(s[i].ToString() + s[i + 1].ToString()) > -1)
            {
                hasRightPair = true;
            }
        }
        catch (Exception)
        {
            Console.WriteLine('2');
            throw;
        }

    }
    if(!hasLetterRepeat || !hasRightPair) { return false; }
    return true;
}
