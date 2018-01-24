all: clean
	gcc ./pollards_rho.c -o pollards_rho

clean:
	rm -rf ./pollards_rho
