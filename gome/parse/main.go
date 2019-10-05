package main

import (
	"encoding/json"
	"fmt"
)

type Student struct {
	FirstName   string `json:"first_name"`
	LastName    string `json:"last_name"`
	Email       string `json:"email"`
	Age         int    `json:"age"`
	ClassName   string `json:"course_name"`
	AcademyName string `json:"acedemy_name"`
}

func main() {
	s := string(`{
		"first_name":"Tin",
		"last_name":"Tran",
		"email_address":"tintran@gmail.com",
		"age":80,
		"course_name":"golang0110",
		"acedemy_name":"Nordic Coder"}`)
	data := Student{}

	json.Unmarshal([]byte(s), &data)
	fmt.Printf("FirstName: %s", data.FirstName)
}

