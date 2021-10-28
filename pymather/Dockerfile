# Build container
FROM debian:bullseye AS build

# Setup environment
RUN mkdir -p /data
WORKDIR /data

# Build the release
COPY . .
RUN ./Hydrunfile

# Extract the release
RUN mkdir -p /out
RUN cp out/release/pymather.linux-$(uname -m) /out/pymather

# Release container
FROM debian:bullseye

# Add certificates
RUN apt update
RUN apt install -y ca-certificates

# Add the release
COPY --from=build /out/pymather /usr/local/bin/pymather

CMD /usr/local/bin/pymather
