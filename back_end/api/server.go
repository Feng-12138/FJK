package server

import (
	"context"
	"time"

	"github.com/gin-gonic/gin"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
)

type Server struct {
	mongo *mongo.Client
}

func newServer(mongo *mongo.Client) *Server {
	return &Server{
		mongo: mongo,
	}
}

func connect(uri string) (*mongo.Client, context.Context, context.CancelFunc, error) {
	ctx, cancel := context.WithTimeout(context.Background(), 30*time.Second)
	client, err := mongo.Connect(ctx, options.Client().ApplyURI(uri))
	return client, ctx, cancel, err
}

func (s *Server) RegisterRountes(r gin.IRoutes) {
}
