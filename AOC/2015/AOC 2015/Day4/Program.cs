using System.Security.Cryptography;
using System.Text;

string input = "iwrupvqb";

int count = 30000; // Threshold: 9958218

while (true)
{
    string md5Hash = ComputeMD5Hash(input + count.ToString());
    if (md5Hash.Substring(0, 6) == "000000")
    {
        break;
    }
    count++;
}

Console.WriteLine($"Part 2: {count}");
string ComputeMD5Hash(string input)
{
    using (MD5 md5 = MD5.Create())
    {
        byte[] inputBytes = Encoding.UTF8.GetBytes(input);
        byte[] hashBytes = md5.ComputeHash(inputBytes);

        StringBuilder builder = new StringBuilder();
        for (int i = 0; i < hashBytes.Length; i++)
        {
            builder.Append(hashBytes[i].ToString("x2")); // Convert each byte to a 2-digit hexadecimal representation
        }

        return builder.ToString();
    }
}