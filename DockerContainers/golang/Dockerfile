FROM golang:1.21

WORKDIR /Users/ivanildo_barauna/bitbucket_mycodes/_go_learning

# pre-copy/cache go.mod for pre-downloading dependencies and only redownloading them in subsequent builds if they change
COPY go.mod go.sum ./
RUN go mod download && go mod verify

COPY . .
RUN go build -v -o /.main.go/app ./...

CMD ["app"]