# tensorflow-serving-apis-proto

A repository to store tensorflow serving APIs protobuf files.

How to use

1. Just copy files or download from [this link](https://github.com/jeongukjae/tensorflow-serving-apis-proto/releases/tag/2.7.0) and compile those files as usual.
2. [Checkout this link](https://github.com/jeongukjae/chips/tree/main/tfs-go-client-example) if you want to use this with Bazel.

## Bazel usage

### WORKSPACE

```starlark
http_archive(
    name = "com_github_jeongukjae_tfs_proto",
    strip_prefix = "tensorflow-serving-apis-proto-2.7.0",
    url = "https://github.com/jeongukjae/tensorflow-serving-apis-proto/archive/2.7.0.tar.gz",
)
```

### BUILD file

```starlark
# golang example

# tensorflow serving apis
go_proto_library(
    name = "tensorflow_serving_apis_go_proto",
    compiler = "@io_bazel_rules_go//proto:go_grpc",
    importpath = "github.com/tensorflow/serving/tensorflow_serving/apis",
    proto = "@com_github_jeongukjae_tfs_proto//:tensorflow_serving_apis_proto",
    deps = [
        ":tensorflow_core_example_go_proto",
        ":tensorflow_core_framework_go_proto",
        ":tensorflow_core_protobuf_go_proto",
        ":tensorflow_serving_config_go_proto",
    ],
)

go_proto_library(
    name = "tensorflow_serving_config_go_proto",
    importpath = "github.com/tensorflow/serving/tensorflow_serving/config",
    proto = "@com_github_jeongukjae_tfs_proto//:tensorflow_serving_config_proto",
)

# tensorflow protos
go_proto_library(
    name = "tensorflow_core_framework_go_proto",
    importpath = "github.com/tensorflow/tensorflow/tensorflow/go/core/framework",
    proto = "@com_github_jeongukjae_tfs_proto//:tensorflow_core_framework_proto",
)

go_proto_library(
    name = "tensorflow_core_example_go_proto",
    importpath = "github.com/tensorflow/tensorflow/tensorflow/go/core/example",
    proto = "@com_github_jeongukjae_tfs_proto//:tensorflow_core_example_proto",
)

go_proto_library(
    name = "tensorflow_core_protobuf_go_proto",
    importpath = "github.com/tensorflow/tensorflow/tensorflow/go/core/protobuf",
    proto = "@com_github_jeongukjae_tfs_proto//:tensorflow_core_protobuf_proto",
    deps = [
        ":tensorflow_core_framework_go_proto",
    ],
)
```
