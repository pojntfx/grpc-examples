using System;
using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Http;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;

namespace MatherNet
{
    public class Startup
    {
        private readonly IConfiguration Configuration;

        public Startup(IConfiguration configuration)
        {
            Configuration = configuration;
        }

        public void ConfigureServices(IServiceCollection services)
        {
            services.AddGrpc();
            services.AddGrpcReflection();
        }

        public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
        {
            var multiplier = Environment.GetEnvironmentVariable("MULTIPLIER");
            if (string.IsNullOrEmpty(multiplier))
            {
                multiplier = "1";
            }
            Configuration["Multiplier"] = multiplier;

            if (env.IsDevelopment())
            {
                app.UseDeveloperExceptionPage();
            }

            app.UseRouting();

            app.UseEndpoints(endpoints =>
            {
                endpoints.MapGrpcService<MatherService>();

                if (env.IsDevelopment())
                {
                    endpoints.MapGrpcReflectionService();
                }

                endpoints.MapGet("/", async context =>
                {
                    await context.Response.WriteAsync("Communication with gRPC endpoints must be made through a gRPC client. To learn how to create a client, visit: https://go.microsoft.com/fwlink/?linkid=2086909");
                });
            });
        }
    }
}
