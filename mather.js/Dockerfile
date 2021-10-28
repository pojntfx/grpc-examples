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
RUN cp out/release/mather.js.linux-$(uname -m) /out/mather.js

# Release container
FROM debian:bullseye

# Add certificates
RUN apt update
RUN apt install -y ca-certificates

# Add the release
COPY --from=build /out/mather.js /usr/local/bin/mather.js

CMD /usr/local/bin/mather.js
