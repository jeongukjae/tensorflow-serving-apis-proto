#!/bin/bash
set -ex

TF_VERSION=2.7.0
TFS_VERSION=2.7.0
TMP=tmp

function main() {
    target_path=`realpath $1`

    rm -rf $TMP $target_path/tensorflow $target_path/tensorflow_serving
    mkdir -p $TMP $target_path

    fetchTFSApi $target_path/
    fetchTFProto $target_path/

    find $target_path -type d -empty -delete
}

function fetchTFSApi() {
    mkdir -p $TMP/tensorflow-serving
    pushd $TMP/tensorflow-serving

    curl -LS -o serving.zip https://github.com/tensorflow/serving/archive/$TFS_VERSION.zip
    unzip -q serving.zip

    mkdir -p $1/tensorflow_serving
    rsync -r --include "*/" --exclude="internal/*" --include="*.proto" --exclude="*" serving-$TFS_VERSION/tensorflow_serving/apis/ $1/tensorflow_serving/apis/

    popd
}

function fetchTFProto() {
    mkdir -p $TMP/tensorflow
    pushd $TMP/tensorflow

    curl -LS -o tf.zip https://github.com/tensorflow/tensorflow/archive/v$TF_VERSION.zip
    unzip -q tf.zip

    mkdir -p $1/tensorflow/core
    rsync -r --include="*.proto" --exclude="*" tensorflow-$TF_VERSION/tensorflow/core/framework/ $1/tensorflow/core/framework/
    rsync -r --include="*.proto" --exclude="*" tensorflow-$TF_VERSION/tensorflow/core/example/ $1/tensorflow/core/example/
    rsync -r --include="*.proto" --exclude="*" tensorflow-$TF_VERSION/tensorflow/core/protobuf/ $1/tensorflow/core/protobuf/

    popd
}

main $@