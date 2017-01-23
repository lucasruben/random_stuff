using System;
class MainClass {
  public static void Main (string[] args) {
    
    for(int i = 0; i <= 100; i++)
    {
    	if(i < 3)
    	{
    		Console.WriteLine ("{0}", i);
    	}
    	else
    	{ 
    		var mod3 = i % 3 == 0 ? true : false;
    		var mod5 = i % 5 == 0 ? true : false;
    		
    		if(mod3 && mod5)
    		{
    			Console.WriteLine ("ThreeFive");
    		}
    		else if(mod3)
    		{
    			Console.WriteLine ("Three");
    		}
    		else if(mod5)
    		{
    			Console.WriteLine ("Five");
    		}
    		else
    		{
    		    Console.WriteLine ("{0}", i);
    		};		
    	};
    };
  }
}
