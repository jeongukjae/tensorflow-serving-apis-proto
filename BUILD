package(default_visibility = ["//visibility:public"])

proto_library(
    name = "tensorflow_core_framework_proto",
    srcs = glob(["tensorflow/core/framework/**"]),
)

proto_library(
    name = "tensorflow_core_example_proto",
    srcs = glob(["tensorflow/core/example/**"]),
)

proto_library(
    name = "tensorflow_core_protobuf_proto",
    srcs = glob(["tensorflow/core/protobuf/**"]),
    deps = [
        ":tensorflow_core_framework_proto",
        "@com_google_protobuf//:any_proto",
    ]
)

proto_library(
    name = "tensorflow_serving_config_proto",
    srcs = glob(["tensorflow_serving/config/**"]),
    deps = [
        "@com_google_protobuf//:any_proto",
    ],
)

proto_library(
    name = "tensorflow_serving_apis_proto",
    srcs = glob(["tensorflow_serving/apis/**"]),
    deps = [
        ":tensorflow_core_framework_proto",
        ":tensorflow_core_example_proto",
        ":tensorflow_core_protobuf_proto",
        ":tensorflow_serving_config_proto",
        "@com_google_protobuf//:any_proto",
        "@com_google_protobuf//:wrappers_proto",
    ]
)
