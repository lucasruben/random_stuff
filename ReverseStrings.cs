using System;

class MainClass {

  public static string FirstReverse(string str) {
    
    char[] result = str.ToCharArray();
    Array.Reverse(result);
    str = new string(result);

    return str;
  }

  static void Main() {  
    // keep this function call here
    Console.WriteLine(FirstReverse(Console.ReadLine()));
  } 

}
