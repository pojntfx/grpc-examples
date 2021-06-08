all: build

build:
	go build -o out/gomather main.go

release:
	CGO_ENABLED=1 go build -ldflags="-extldflags=-static" -tags netgo -o out/release/gomather.linux-$$(uname -m) main.go

install: release
	sudo install out/release/gomather.linux-$$(uname -m) /usr/local/bin/gomather
	
dev:
	while [ -z "$$PID" ] || [ -n "$$(inotifywait -q -r -e modify pkg main.go)" ]; do\
		$(MAKE);\
		kill -9 $$PID 2>/dev/null 1>&2;\
		wait $$PID;\
		out/gomather & export PID="$$!";\
	done

clean:
	rm -rf out
	rm -rf pkg/api/proto/v1

depend:
	# Setup CLIs
	GO111MODULE=on go get github.com/golang/protobuf/protoc-gen-go@latest
	GO111MODULE=on go get github.com/fullstorydev/grpcurl/cmd/grpcurl@latest
	# Generate bindings
	go generate ./...	