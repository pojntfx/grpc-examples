# Generated by the protocol buffer compiler.  DO NOT EDIT!
# Source: proto/mather.proto for package 'com.pojtinger.felix.grpcExamples.gomather'

require 'grpc'
require 'proto/mather_pb'

module Com
  module Pojtinger
    module Felix
      module GrpcExamples
        module Gomather
          module Mather
            class Service

              include ::GRPC::GenericService

              self.marshal_class_method = :encode
              self.unmarshal_class_method = :decode
              self.service_name = 'com.pojtinger.felix.grpcExamples.gomather.Mather'

              rpc :Add, ::Com::Pojtinger::Felix::GrpcExamples::Gomather::AddInputMessage, ::Com::Pojtinger::Felix::GrpcExamples::Gomather::AddOutputMessage
            end

            Stub = Service.rpc_stub_class
          end
        end
      end
    end
  end
end
