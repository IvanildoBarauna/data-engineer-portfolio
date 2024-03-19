package main

import (
	"fmt"
	"time"
)

type dog struct {
	name string
}

func (d dog) BauAuAu() {
	fmt.Println(d.name, " BauAuAu")
}

func counter(count int) {
	for i := 1; i < count; i++ {
		time.Sleep(1 * time.Second)
		fmt.Println(i)
	}

}

func main() {
	var myDog dog

	myDog.name = "Benaia"

	myDog.BauAuAu()

	go counter(10)
	go counter(10)
	counter(10)
}
