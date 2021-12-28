#!/bin/bash

for file in tensorflow/core/**/*.proto ; do
    sed -i '' -E 's/(option go_package.+)\/[^\/]+";/\1";/' $file
done
