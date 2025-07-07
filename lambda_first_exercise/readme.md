# Create Lambda layer for sklearn

Commands to run to generate the layer zip file
```
docker build -t lambda-layer-builder .

docker run --name extract-layer lambda-layer-builder
docker cp extract-layer:/layer/layer.zip .
docker rm extract-layer
```
