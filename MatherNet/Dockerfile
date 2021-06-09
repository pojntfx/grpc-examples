# Build container
FROM mcr.microsoft.com/dotnet/sdk:5.0-buster-slim-amd64 AS build

# Setup environment
RUN mkdir -p /data
WORKDIR /data
ARG TARGETPLATFORM

# Build the release
COPY . .
RUN ./Hydrunfile

# Extract the release
RUN mkdir -p /out
RUN cp out/release/MatherNet.linux-${TARGETPLATFORM} /out/MatherNet

# Release container
FROM debian

# Add certificates
RUN apt update
RUN apt install -y ca-certificates

# Add the release
COPY --from=build /out/MatherNet /usr/local/bin/MatherNet

CMD /usr/local/bin/MatherNet
