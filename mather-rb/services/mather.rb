this_dir = File.expand_path(File.dirname(__FILE__))
$LOAD_PATH.unshift(File.join(this_dir, '..'))

require 'proto/mather_services_pb'
require 'proto/mather_pb'
require 'grpc'

class MatherService < Com::Pojtinger::Felix::GrpcExamples::Gomather::Mather::Service
    def add(req, _)
        Com::Pojtinger::Felix::GrpcExamples::Gomather::AddOutputMessage.new(Sum: req.FirstSummand + req.SecondSummand)
    end
end