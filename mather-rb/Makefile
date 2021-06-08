all: build

build:
	# Create dynamically-linked binary
	mkdir -p /tmp/out
	rubyc bin/mather-rb -o /tmp/out/mather-rb.linux-$$(uname -m)

	# Stage dynamically-linked binaries
	mkdir -p out
	cp /tmp/out/mather-rb.linux-$$(uname -m) out

release: build
	# Create statically-linked binary
	mkdir -p /tmp/out/release
	staticx /tmp/out/mather-rb.linux-$$(uname -m) /tmp/out/release/mather-rb.linux-$$(uname -m)

	# Stage statically-linked binaries
	mkdir -p out/release
	cp /tmp/out/release/mather-rb.linux-$$(uname -m) out/release

install: release
	sudo install out/release/mather-rb.linux-$$(uname -m) /usr/local/bin/mather-rb

dev:
	bundle exec ruby main.rb

clean:
	rm proto/mather*.rb
	rm -rf out

depend:
	# Install dependencies
	bundle install

	# Install development dependencies
	pip3 install staticx

	# Generate Protobufs
	grpc_tools_ruby_protoc --ruby_out=./ --grpc_out=./ ./proto/mather.proto