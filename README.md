# gRPC Examples

gRPC example microservices in Go, Rust, C#, Python and JavaScript.

[![hydrun CI](https://github.com/pojntfx/grpc-examples/actions/workflows/hydrun.yaml/badge.svg)](https://github.com/pojntfx/grpc-examples/actions/workflows/hydrun.yaml)
[![Docker CI](https://github.com/pojntfx/grpc-examples/actions/workflows/docker.yaml/badge.svg)](https://github.com/pojntfx/grpc-examples/actions/workflows/docker.yaml)
[![Matrix](https://img.shields.io/matrix/grpc-examples:matrix.org)](https://matrix.to/#/#grpc-examples:matrix.org?via=matrix.org)

## Overview

This repo includes very simple example math gPRC microservices in multiple languages. They can be used to get started with gRPC and Kubernetes, be used as a reference, or as a template for your own service.

Currently, the following example services have been added; please check out their individual READMEs for more information on them:

| Icon                                                                                                                      | Name                       | Link                            |
| ------------------------------------------------------------------------------------------------------------------------- | -------------------------- | ------------------------------- |
| <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/go/go-original.svg" width="25">                 | **gomather (Go)**          | [README](./gomather/README.md)  |
| <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/rust/rust-plain.svg" width="25">                | **mather-rs (Rust)**       | [README](./mather-rs/README.md) |
| <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/csharp/csharp-original.svg" width="25">         | **MatherNew (C#)**         | [README](./MatherNet/README.md) |
| <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" width="25">         | **pymather (Python)**      | [README](./pymather/README.md)  |
| <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" width="25"> | **mather.js (JavaScript)** | [README](./mather.js/README.md) |

📖 **Happy learning**!

## Contributing

To contribute, please use the [GitHub flow](https://guides.github.com/introduction/flow/) and follow our [Code of Conduct](../CODE_OF_CONDUCT.md).

To build and start a development version of a microservice locally, run the following:

```shell
$ git clone https://github.com/pojntfx/grpc-examples.git
$ cd service_you_want_contribute_to
$ make depend
$ MULTIPLIER=1 make dev
# Or, if you prefer to develop in Kubernetes
$ MULTIPLIER=1 skaffold dev -p dev --port-forward
```

The microservice should now be started and the frontend be available on `localhost:5000`. Whenever you change a source file, it will automatically be re-compiled.

Have any questions or need help? Chat with us [on Matrix](https://matrix.to/#/#grpc-examples:matrix.org?via=matrix.org)!

## License

gRPC Examples (c) 2021 Felix Pojtinger and contributors

SPDX-License-Identifier: AGPL-3.0
