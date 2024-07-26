all: protoc protoc-ruby

protoc:
	python -m grpc_tools.protoc --proto_path=proto --python_out=. --pyi_out=. --grpc_python_out=. proto/crewgen/proto/crewgenerator.proto

protoc-ruby:
	grpc_tools_ruby_protoc --proto_path=proto/crewgen --ruby_out=proto/ruby --grpc_out=proto/ruby proto/crewgen/proto/crewgenerator.proto
	[ -e `which rubocop` ] && rubocop -A proto/ruby || true
