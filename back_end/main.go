package main

import (
	"context"
	"fmt"

	"github.com/gin-gonic/gin"

	"github.com/Feng-12138/YJK/back_end/server/api"
	"github.com/Feng-12138/YJK/back_end/server/mongodb"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
)

func getURI() string {
	return "mongodb+srv://Feng-12138:2005yyds@cluster0.mnj5ncy.mongodb.net/?retryWrites=true&w=majority"
}

func connect(uri string) *mongo.Client {
	client, err := mongo.Connect(context.TODO(), options.Client().ApplyURI(uri))
	if err != nil {
		fmt.Printf("ERROR: Failed to connect to MongoDB with URI: %s\n", uri)
		panic(err)
	}
	return client
}

func main() {
	uri := getURI()
	db := connect(uri)
	mongo := mongodb.NewStore(db)
	server := api.NewServer(mongo)
	router := gin.Default()
	server.RegisterRoutes(router)
	router.Run("localhost:8080")
}
