package mongodb

import (
	"context"
	"fmt"

	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/mongo"
)

type Store struct {
	db *mongo.Client
}

func NewStore(db *mongo.Client) *Store {
	return &Store{
		db: db,
	}
}

func (s *Store) GetUsers() {
	user := s.db.Database("customer_facing").Collection("user")
	filter := bson.D{{}}
	query, err := user.Find(context.TODO(), filter)
	if err != nil {
		return
	}
	fmt.Println(query)
	var result []bson.M
	query.All(context.TODO(), &result)
	fmt.Print(result)
}
