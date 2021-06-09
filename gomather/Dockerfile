# Build container
FROM debian AS build

# Setup environment
RUN mkdir -p /data
WORKDIR /data

# Build the release
COPY . .
RUN ./Hydrunfile

# Extract the release
RUN mkdir -p /out
RUN cp out/release/gomather.linux-$(uname -m) /out/gomather

# Release container
FROM debian

# Add certificates
RUN apt update
RUN apt install -y ca-certificates

# Add the release
COPY --from=build /out/gomather /usr/local/bin/gomather

CMD /usr/local/bin/gomather
