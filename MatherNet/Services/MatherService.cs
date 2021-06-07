using System.Threading.Tasks;
using Com.Pojtinger.Felix.GrpcExamples.Gomather;
using Grpc.Core;

namespace MatherNet
{
    public class MatherService : Mather.MatherBase
    {
        public override Task<AddOutputMessage> Add(AddInputMessage request, ServerCallContext context)
        {
            return Task.FromResult(new AddOutputMessage
            {
                Sum = request.FirstSummand + request.SecondSummand
            });
        }
    }
}
