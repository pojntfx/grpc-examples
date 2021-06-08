all: build

build:
	# Create and stage dynamically-linked binary
	mkdir -p out
	if [ "$$(uname -m)" = 'x86_64' ]; then\
    	dotnet publish -c Release -r linux-x64 -p:PublishReadyToRun=true -p:PublishSingleFile=true -p:PublishTrimmed=true --self-contained true -p:IncludeNativeLibrariesForSelfExtract=true;\
		cp bin/Release/net5.0/linux-x64/publish/MatherNet out/MatherNet.linux-$$(uname -m);\
	elif [ "$$(uname -m)" = 'armv7l' ]; then\
	    dotnet publish -c Release -r linux-arm64 -p:PublishReadyToRun=true -p:PublishSingleFile=true -p:PublishTrimmed=true --self-contained true -p:IncludeNativeLibrariesForSelfExtract=true;\
		cp bin/Release/net5.0/linux-arm64/publish/MatherNet out/MatherNet.linux-$$(uname -m);\
	else\
	    dotnet publish -c Release -r linux-arm -p:PublishReadyToRun=true -p:PublishSingleFile=true -p:PublishTrimmed=true --self-contained true -p:IncludeNativeLibrariesForSelfExtract=true;\
		cp bin/Release/net5.0/linux-arm/publish/MatherNet out/MatherNet.linux-$$(uname -m);\
	fi;
	
release: build
	# Stage dynamically-linked binaries
	mkdir -p out/release
	cp out/MatherNet.linux-$$(uname -m) out/release

install: release
	sudo install out/release/MatherNet.linux-$$(uname -m) /usr/local/bin/MatherNet

dev:
	dotnet watch run

clean:
	rm -rf out

depend:
	# Install dependencies
	dotnet restore
