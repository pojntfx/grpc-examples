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
RUN if [ "${TARGETPLATFORM}" = "linux/amd64" ]; then \
        RID=x86_64; \
    elif [ "${TARGETPLATFORM}" = "linux/arm64" ]; then \
        RID=aarch64; \
    elif [ "${TARGETPLATFORM}" = "linux/arm/v7" ]; then \
        RID=armv7l; \
    fi \
    && cp out/release/MatherNet.linux-${RID} /out/MatherNet

# Release container
FROM debian

# Add certificates
RUN apt update
RUN apt install -y ca-certificates libicu63 libgssapi-krb5-2

# Add the release
COPY --from=build /out/MatherNet /usr/local/bin/MatherNet

CMD /usr/local/bin/MatherNet
