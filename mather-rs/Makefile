all: build

build:
	# Create statically-linked binary
	mkdir -p /tmp/out
	cargo build --release

	# Stage statically-linked binaries
	mkdir -p out
	cp target/release/mather-rs out/mather-rs.linux-$$(uname -m)

release: build
	# Stage statically-linked binaries
	mkdir -p out/release
	cp out/mather-rs.linux-$$(uname -m) out/release

install: release
	sudo install out/release/mather-rs.linux-$$(uname -m) /usr/local/bin/mather-rs

dev:
	cargo run

clean:
	rm -rf out

depend:
	# Install dependencies
	cargo build
