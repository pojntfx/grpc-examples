package main

import (
	"log"
	"net"
	"os"

	api "github.com/pojntfx/grpc-examples/gomather/pkg/api/proto/v1"
	"github.com/pojntfx/grpc-examples/gomather/pkg/services"
	"google.golang.org/grpc"
	"google.golang.org/grpc/reflection"
)

func main() {
	laddr := os.Getenv("LADDR")
	if laddr == "" {
		laddr = "0.0.0.0:5000"
	}

	lis, err := net.Listen("tcp", laddr)
	if err != nil {
		panic(err)
	}

	srv := grpc.NewServer()
	reflection.Register(srv)
	api.RegisterMatherServer(srv, &services.MatherService{})

	log.Println("Listening on", laddr)

	panic(srv.Serve(lis))
}
