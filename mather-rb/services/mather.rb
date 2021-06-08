this_dir = File.expand_path(File.dirname(__FILE__))
$LOAD_PATH.unshift(File.join(this_dir, '..'))

require 'proto/mather_services_pb'
require 'proto/mather_pb'
require 'grpc'

class MatherService < Com::Pojtinger::Felix::GrpcExamples::Mather::Service
    def initialize(multiplier)
        @multiplier = multiplier.to_i
    end

    def add(req, _)
        Com::Pojtinger::Felix::GrpcExamples::AddOutputMessage.new(Sum: (req.FirstSummand + req.SecondSummand) * @multiplier)
    end
end