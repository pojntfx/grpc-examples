dev:
	bundle exec ruby main.rb

clean:
	rm proto/mather*.rb

depend:
	# Install dependencies
	bundle install

	# Generate Protobufs
	grpc_tools_ruby_protoc --ruby_out=./ --grpc_out=./ ./proto/mather.proto