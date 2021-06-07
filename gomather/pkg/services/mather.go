package services

import (
	"context"

	api "github.com/pojntfx/grpc-examples/gomather/pkg/api/proto/v1"
)

//go:generate sh -c "mkdir -p ../api/proto/v1 && protoc --go_out=paths=source_relative,plugins=grpc:../api/proto/v1 -I=../../api/proto/v1 ../../api/proto/v1/*.proto"

type MatherService struct {
	api.UnimplementedMatherServer
}

func (s *MatherService) Add(_ context.Context, aim *api.AddInputMessage) (*api.AddOutputMessage, error) {
	return &api.AddOutputMessage{
		Sum: aim.FirstSummand + aim.SecondSummand,
	}, nil
}
