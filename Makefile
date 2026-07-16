all: build run

build:
	cargo build --release
	copy target\release\rust_motor.dll target\release\rust_motor.pyd

run:
	python app/main.py

clean:
	cargo clean