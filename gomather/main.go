package main

import (
	"log"
	"net"
	"os"
	"strconv"

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

	multiplierRaw := os.Getenv("MULTIPLIER")
	if multiplierRaw == "" {
		multiplierRaw = "1"
	}

	multiplier, err := strconv.Atoi(multiplierRaw)
	if err != nil {
		panic(err)
	}

	lis, err := net.Listen("tcp", laddr)
	if err != nil {
		panic(err)
	}

	srv := grpc.NewServer()
	reflection.Register(srv)
	api.RegisterMatherServer(srv, &services.MatherService{
		Multiplier: int64(multiplier),
	})

	log.Println("Listening on", laddr)

	panic(srv.Serve(lis))
}
