# Commands to run container locally
if [ ! "$(docker ps -q -f name=webapp)" ]; then
    if [ "$(docker ps -aq -f status=exited -f name=webapp)" ]; then
        # cleanup
        docker rm webapp
        # docker image prune
    fi
    docker build -t app-container .
    # run your container
    docker run -p 5000:5000 --name webapp app-container
    # can use -d option to create detached container
fi
