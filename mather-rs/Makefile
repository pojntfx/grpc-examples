all: build

build:
	# Create dynamically-linked binary
	mkdir -p /tmp/out
	cargo build --release

	# Stage dynamically-linked binaries
	mkdir -p out
	cp target/release/mather-rs out/mather-rs.linux-$$(uname -m)

release: build
	# Create statically-linked binary
	mkdir -p /tmp/out/release
	staticx out/mather-rs.linux-$$(uname -m) /tmp/out/release/mather-rs.linux-$$(uname -m)

	# Stage statically-linked binaries
	mkdir -p out/release
	cp /tmp/out/release/mather-rs.linux-$$(uname -m) out/release

install: release
	sudo install out/release/mather-rs.linux-$$(uname -m) /usr/local/bin/mather-rs

dev:
	cargo run

clean:
	rm -rf out

depend:
	# Install dependencies
	cargo build

	# Install development dependencies
	pip3 install staticx
