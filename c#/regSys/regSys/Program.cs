using Microsoft.VisualBasic.CompilerServices;
using regSys;
using System;
using System.IO;

namespace regSys
{
	class Program
	{
		
		static void Main(string[] args)
		{	
			createUserFilesDir();
			User Felhasznalo = new User("Gote", "asd");
			makeUserFile(Felhasznalo.username);
		}

		private static void print(string stuff)
        {
			Console.WriteLine(stuff);
        }

		private static void debug(string data)
        {
			if (Globals.DEBUG)
            {
				print(data);
            }
        }
		private static void createUserFilesDir()
		{
			// This method creates the userFiles directory in the cwd 
			
			Console.WriteLine(Globals.USER_FILES_PATH);

            if (!Directory.Exists(Globals.USER_FILES_PATH))
            {
				Directory.CreateDirectory(Globals.USER_FILES_PATH);
				debug("created user files directory");
			}
			
		   
		}   
		private static void makeUserFile(string username)
        {
			// This method creates the user's file (userFiles\\username_File)
			Directory.CreateDirectory(Globals.USER_FILES_PATH + "\\" + username + "_File");
			string userFile = Globals.USER_FILES_PATH + "\\" + username + "_File" + "\\" + username + "_Data.txt";
			if (!File.Exists(userFile))
            {
				File.WriteAllText(userFile, "ya made it boi");
				debug("created user file: " + username);
			}
			

        }
		private static string[] register(string username, string password)
		{
			string[] userData = { username, password };
			return userData;
				
		}

	}   




}

