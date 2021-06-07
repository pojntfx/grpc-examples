all: build

build:
	# Create dynamically-linked binary
	mkdir -p /tmp/out
	mkdir -p /tmp/build/build-$$(uname -m)
	mkdir -p /tmp/spec/spec-$$(uname -m)
	pyinstaller -n pymather.linux-$$(uname -m) --distpath /tmp/out --workpath /tmp/build/build-$$(uname -m) --specpath /tmp/spec/spec-$$(uname -m) --onefile main.py

	# Stage dynamically-linked binaries
	mkdir -p out
	cp /tmp/out/pymather.linux-$$(uname -m) out

release: build
	# Create statically-linked binary
	mkdir -p /tmp/out/release
	staticx /tmp/out/pymather.linux-$$(uname -m) /tmp/out/release/pymather.linux-$$(uname -m)

	# Stage statically-linked binaries
	mkdir -p out/release
	cp /tmp/out/release/pymather.linux-$$(uname -m) out/release

install: release
	sudo install out/release/pymather.linux-$$(uname -m) /usr/local/bin/pymather
	
dev:
	python3 main.py

clean:
	rm -rf pymather/proto/mather*.py
	rm -rf out

depend:
	# Install dependencies
	pip3 install -r requirements.txt

	# Install python development dependencies
	pip3 install pyinstaller
	pip3 install staticx

	# Generate Protobufs
	python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./pymather/proto/mather.proto
