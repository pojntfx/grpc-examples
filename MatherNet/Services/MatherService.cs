using System.Threading.Tasks;
using Com.Pojtinger.Felicitas.GrpcExamples;
using Grpc.Core;
using Microsoft.Extensions.Configuration;

namespace MatherNet
{
    public class MatherService : Mather.MatherBase
    {
        private readonly int Multiplier;

        public MatherService(IConfiguration configuration)
        {
            Multiplier = int.Parse(configuration["Multiplier"]);
        }

        public override Task<AddOutputMessage> Add(AddInputMessage request, ServerCallContext context)
        {
            return Task.FromResult(new AddOutputMessage
            {
                Sum = (request.FirstSummand + request.SecondSummand) * Multiplier
            });
        }
    }
}
