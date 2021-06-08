all: build

build:
	# Create and stage dynamically-linked binary
	yarn build

release: build
	# Stage dynamically-linked binaries
	mkdir -p out/release
	cp out/mather.js.linux-$$(uname -m) out/release

install: release
	sudo install out/release/mather.js.linux-$$(uname -m) /usr/local/bin/mather.js
	
dev:
	yarn start

clean:
	yarn clean

depend:
	# Install dependencies
	yarn

	# Generate Protobufs
	yarn generate
