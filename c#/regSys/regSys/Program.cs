using System;
using System.IO;


// TODO
// Need a main loop. breaks when exit or acc deleted
// work out json parsing
// dont wake up

namespace regSys
{
    class Program
    {

        static void Main()
        {
            makeDatabase(Globals.CWD);
            createUserFilesDir();
            
            
            string enteredChoice = welcomePrompt();
            if (enteredChoice == "1")
                //Login
            {
                string[] creds = getLogin(input("Enter your username: "), input("password: "));
                User Felhasznalo = new User(creds[0], creds[1]);
                debug("created user obj\n u: " + creds[0] + "\np: " + creds[1]);

            }
            else if (enteredChoice == "2")
                //Register
            {



                //User.makeUserFile(Felhasznalo.username);
            }
            else if (enteredChoice == "0")
                //Exit
            {
                
            }
            
        }

        public static void print(string stuff)
        {
            Console.WriteLine(stuff);
        }

        public static string input(string stuff)
        {
            print(stuff);
            string data = Console.ReadLine().ToString();
            return data;
        }

        public static void debug(string data)
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

        private static void makeDatabase(string location)
        {
            location = location + "database.txt";
            if (!File.Exists(location))
            {
                File.WriteAllText(location, "ya made it boi");
                debug("created database file");
            }
        }

        private static string welcomePrompt()
        {
            print("-----" + "WELCOME" + "-----");
            print("1 | Login");
            print("2 | Register");
            print("0 | Exit");
            string enteredChoice = input("choice: ");
            return enteredChoice;
        }

        private static string[] getLogin(string username, string password)
        {
            // usercreds[0] -> username
            // usercreds[1] -> password
            string usrName = username;
            string pw = password;
            string[] userCreds = { usrName, pw };
            return userCreds;
        }


    }




}

