using System;
using Microsoft.AspNetCore.Hosting;
using Microsoft.Extensions.Hosting;

namespace MatherNet
{
    public class Program
    {
        public static void Main(string[] args)
        {
            CreateHostBuilder(args).Build().Run();
        }

        public static IHostBuilder CreateHostBuilder(string[] args)
        {
            var laddr = Environment.GetEnvironmentVariable("LADDR");

            return Host.
                CreateDefaultBuilder(args)
                .ConfigureWebHostDefaults(webBuilder =>
                {
                    webBuilder.UseStartup<Startup>();

                    if (!String.IsNullOrEmpty(laddr))
                    {
                        webBuilder.UseUrls("http://" + laddr + "/");
                    }
                });
        }
    }
}
