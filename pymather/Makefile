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
	# Stage statically-linked binaries
	mkdir -p out/release
	cp out/pymather.linux-$$(uname -m) out/release

install: release
	sudo install out/release/pymather.linux-$$(uname -m) /usr/local/bin/pymather
	
dev:
	while [ -z "$$PID" ] || [ -n "$$(inotifywait -q -r -e modify main.py pymather)" ]; do\
		kill -9 $$PID 2>/dev/null 1>&2;\
		wait $$PID;\
		python3 main.py & export PID="$$!";\
	done

clean:
	rm pymather/proto/mather*.py
	rm -rf out

depend:
	# Update pip for much faster grpcio builds
	pip3 install --upgrade pip

	# Install dependencies
	pip3 install -r requirements.txt

	# Install python development dependencies
	pip3 install pyinstaller

	# Generate Protobufs
	python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./pymather/proto/mather.proto
