package api

import (
	"github.com/Feng-12138/YJK/back_end/server/mongodb"
	"github.com/gin-gonic/gin"
)

type Server struct {
	mongo mongodb.DB
}

func NewServer(mongo mongodb.DB) *Server {
	return &Server{
		mongo: mongo,
	}
}

func (s *Server) RegisterRoutes(router gin.IRouter) {
	router.GET("/", s.handleGetUsers)
}

func (s *Server) handleGetUsers(c *gin.Context) {
	s.mongo.GetUsers()
}
