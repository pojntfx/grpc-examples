all: build

build:
	# Create statically-linked binary
	mkdir -p /tmp/out
	cargo build --release

	# Stage statically-linked binaries
	mkdir -p out
	cp target/release/mather-rs out/mather-rs

release: build
	# Stage statically-linked binaries
	mkdir -p out/release
	cp out/mather-rs out/release/mather-rs.linux-$$(uname -m)

install: release
	sudo install out/release/mather-rs.linux-$$(uname -m) /usr/local/bin/mather-rs

dev:
	while [ -z "$$PID" ] || [ -n "$$(inotifywait -q -r -e modify proto src)" ]; do\
		$(MAKE);\
		kill -9 $$PID 2>/dev/null 1>&2;\
		wait $$PID;\
		out/mather-rs & export PID="$$!";\
	done

clean:
	rm -rf out

depend:
	# Install dependencies
	cargo build
