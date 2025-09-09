FROM swift:latest

WORKDIR /app

COPY . .

RUN swift build
CMD ["swift", "test"]
# docker build -t swift-algorithms .
# docker run --rm swift-algorithms