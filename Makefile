run:
	python code/main.py

clean:
	rm -rf __pycache__ *.log *.aux *.out *.toc *.pdf figures/*.png

paper:
	pandoc paper.md -o paper.pdf
