this_dir = File.expand_path(File.dirname(__FILE__))
$LOAD_PATH.unshift(File.join(this_dir, 'services'))

require 'grpc'
require 'mather'

laddr = ENV['LADDR'] || '0.0.0.0:5000'

srv = GRPC::RpcServer.new
srv.add_http2_port(laddr, :this_port_is_insecure)
srv.handle(MatherService)

puts "Listening on #{laddr}"

srv.run_till_terminated_or_interrupted([1, 'int', 'SIGQUIT'])