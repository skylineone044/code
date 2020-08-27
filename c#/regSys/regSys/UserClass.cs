using System.IO;

namespace regSys

{

    class User
    {
        public string username;
        public string password;
        public string auth;

        public User(string aUsername, string aPassword)
        {
            username = aUsername;
            password = aPassword;
        }

        public static void makeUserFile(string username)
        {
            // This method creates the user's file (userFiles\\username_File)
            Directory.CreateDirectory(Globals.USER_FILES_PATH + "\\" + username + "_File");
            string userFile = Globals.USER_FILES_PATH + "\\" + username + "_File" + "\\" + username + "_Data.txt";
            if (!File.Exists(userFile))
            {
                File.WriteAllText(userFile, "ya made it boi");
                Program.debug("created user file: " + username);
            }


        }

        public static string[] register(string username, string password)
        {
            string[] userData = { username, password };
            return userData;

        }



    }
}