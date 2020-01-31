package main

import(
    "fmt"
    "os"
)

func checkError(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	f, err := os.Create("./test.md")
	checkError(err)

	defer f.Close()

	test, err := f.WriteString("this is a a string")
	checkError(err)

	fmt.Printf("Done son. %o", test)
}
