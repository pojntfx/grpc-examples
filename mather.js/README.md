# mather.js

Simple JavaScript gRPC microservice that does math.

[![Docker Pulls](https://img.shields.io/docker/pulls/pojntfx/mather-js?label=docker%20pulls)](https://hub.docker.com/r/pojntfx/mather-js)
[![Binary Downloads](https://img.shields.io/github/downloads/pojntfx/grpc-examples/latest/mather.js.linux-x86_64?label=binary%20downloads)](https://github.com/pojntfx/grpc-examples/releases)

> Be sure to also check out the [other gRPC examples](../README.md) for more information on how to contribute and more!

## Installation

### Kubernetes

You can add the chart repo like so:

```shell
$ helm repo add pojntfx https://pojntfx.github.io/charts/
```

### Containerized

You can get the Docker container like so:

```shell
$ docker pull ghcr.io/pojntfx/mather-js
```

### Natively

If you prefer a native installation, binaries are also available on [GitHub releases](https://github.com/pojntfx/grpc-examples/releases).

You can install them like so:

```shell
$ curl -L -o /tmp/mather.js https://github.com/pojntfx/grpc-examples/releases/latest/download/mather.js.linux-$(uname -m)
$ sudo install /tmp/mather.js /usr/local/bin
```

## Usage

### 1 (Option 1): Starting the Microservice (Kubernetes)

Helm is the easiest option to start the microservice on Kubernetes.

<details>
  <summary>Expand installation instructions</summary>

Run the following; see the [Reference](#reference) for more configuration parameters:

```shell
$ helm install mather-js pojntfx/mather-js --set app.multiplier=1
```

The logs are available like so:

```shell
$ kubectl logs mather-js
```

  </details>

### 1 (Option 2): Starting the Microservice (Containerized)

Using Docker (or an alternative like Podman) is also possible.

<details>
  <summary>Expand installation instructions</summary>

Run the following; see the [Reference](#reference) for more configuration parameters:

```shell
$ docker run \
    --name mather-js \
    -d \
    --restart always \
    -p 5000:5000 \
    -e MULTIPLIER=1 \
    ghcr.io/pojntfx/mather-js
```

The logs are available like so:

```shell
$ docker logs mather-js
```

  </details>

### 1 (Option 3): Starting the Microservice (Natively)

If you prefer a native setup, a non-containerized installation is also possible.

<details>
  <summary>Expand installation instructions</summary>

First, create a systemd service for it; see the [Reference](#reference) for more configuration parameters::

```shell
$ mkdir -p ~/.config/systemd/user/
$ cat <<EOT >~/.config/systemd/user/mather-js.service
[Unit]
Description=mather.js

[Service]
Environment="MULTIPLIER=1"
ExecStart=/usr/local/bin/mather-js

[Install]
WantedBy=multi-user.target
EOT
```

Finally, reload systemd and enable the service:

```shell
$ systemctl --user daemon-reload
$ systemctl --user enable --now mather-js
```

You can get the logs like so:

```shell
$ journalctl --user -u mather-js
```

  </details>

### 2. Making a Request

Now that the microservice is running, run a request to test it:

```shell
grpcurl --plaintext --proto proto/mather.proto -d '{"FirstSummand": 1, "SecondSummand": 3}' localhost:5000 com.pojtinger.felicitas.grpcExamples.Mather.Add
```

🚀 **That's it**! We hope you enjoy using mather.js.

## Reference

### Environment Variables

You can set the multiplier, which multiplies each sum, using the `MULTIPLIER` environment variable.

If you're on Kubernetes, also check out the available [Helm chart values](./charts/mather-js/values.yaml) which you can use to adjust available resources, set the domain name and more.

### gRPC API

mather.js exposes a gRPC API. You can find the relevant `.proto` files in [proto](./proto).

## License

mather.js (c) 2021 Felicitas Pojtinger and contributors

SPDX-License-Identifier: AGPL-3.0
