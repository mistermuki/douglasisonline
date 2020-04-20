using System;
using System.Threading.Tasks;
using System.Timers;
using System.Threading;
using Tweetinvi;
using System.IO;

// Douglas Is Online (Kessec)
// Made by @mooksmonster & @danturs
// Version: 1.0.1

namespace douglasisonline
{
    class Program
    {
        public static int sentence_struct = 0;


        static void Main(string[] args)
        {
            Auth.SetUserCredentials("4MWWQHdsbatnBvEagSl1uB9OZ", "5HEB4M35aH51YnxrPqGmsf21zk1nyDsE7ZNhn4B2IwLCBvLen0", "1187492688938975232-h4th2vLBh09NlgH0s9EO1e51CHrrCi", "MlXkUUNmyduJYHi6EQmIgU8XV8Jq8Cuvbt6fyQmLesMIr");
            Console.WriteLine("Douglas has been reborn.");
            Console.WriteLine("Version 1.0.1");

            while (true)
            {
                string[] sentences = File.ReadAllLines("F:/Github/douglasisonline/text/sentence.txt");
                string[] noun = File.ReadAllLines("F:/Github/douglasisonline/text/noun.txt");
                string[] verb = File.ReadAllLines("F:/Github/douglasisonline/text/verb.txt");
                string[] adj = File.ReadAllLines("F:/Github/douglasisonline/text/adjective.txt");

                string word1 = "a";
                string word2 = "a";
                string word3 = "a";
                string word4 = "a";

                Random rnd = new Random();


                int sentence_value = rnd.Next(0, sentences.Length);
                bool convert_to_int_sentence = Int32.TryParse(sentences[sentence_value], out sentence_struct);

                if (convert_to_int_sentence == false)
                {
                    Console.WriteLine("Parsing Expection: Converting Sentence to Int");
                }
                else
                {
                    int first = sentence_struct / 1000;
                    int second = (sentence_struct - first * 1000) / 100;
                    int third = (sentence_struct - first * 1000 - second * 100) / 10;
                    int fourth = (sentence_struct - first * 1000 - second * 100 - third * 10) / 1;

                    if (first == 1)
                    {
                        int noun_value1 = rnd.Next(0, noun.Length);
                        word1 = noun[noun_value1];
                    }

                    if (first == 2)
                    {
                        int verb_value1 = rnd.Next(0, verb.Length);
                        word1 = verb[verb_value1];
                    }

                    if (first == 3)
                    {
                        int adj_value1 = rnd.Next(0, adj.Length);
                        word1 = adj[adj_value1];
                    }

                    if (second == 1)
                    {
                        int noun_value2 = rnd.Next(0, noun.Length);
                        word2 = noun[noun_value2];
                    }

                    if (second == 2)
                    {
                        int verb_value2 = rnd.Next(0, verb.Length);
                        word2 = verb[verb_value2];
                    }

                    if (second == 3)
                    {
                        int adj_value2 = rnd.Next(0, adj.Length);
                        word2 = adj[adj_value2];
                    }

                    if (third == 1)
                    {
                        int noun_value3 = rnd.Next(0, noun.Length);
                        word3 = noun[noun_value3];
                    }

                    if (third == 2)
                    {
                        int verb_value3 = rnd.Next(0, verb.Length);
                        word2 = verb[verb_value3];
                    }

                    if (third == 3)
                    {
                        int adj_value3 = rnd.Next(0, adj.Length);
                        word3 = adj[adj_value3];
                    }

                    if (fourth == 1)
                    {
                        int noun_value4 = rnd.Next(0, noun.Length);
                        word4 = noun[noun_value4];
                    }

                    if (fourth == 2)
                    {
                        int verb_value4 = rnd.Next(0, verb.Length);
                        word4 = verb[verb_value4];

                    }

                    if (fourth == 3)
                    {
                        int adj_value4 = rnd.Next(0, adj.Length);
                        word4 = adj[adj_value4];
                    }

                    Console.WriteLine("Tweeted Out:" + " " + word1 + " " + word2 + " " + word3 + " " + word4);
                    Tweet.PublishTweet(word1 + " " + word2 + " " + word3 + " " + word4);
                    Thread.Sleep(1200000);
                }
            }

        }

    }
}
