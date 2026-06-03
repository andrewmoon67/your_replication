.PHONY: all clean

all: paper/paper.pdf

# Step 1: Preprocessing — reads from input/, writes to temp/
temp/clean_data.csv: input/region_level_cumulative.dta code/preprocess.py
	python3 code/preprocess.py

# Step 2: Analysis — reads from temp/, writes to output/
output/tables/main_result.tex: temp/clean_data.csv code/analysis.py
	python3 code/analysis.py

# Step 3: Paper compilation — reads table, produces PDF
paper/paper.pdf: paper/paper.tex output/tables/main_result.tex
	cd paper && pdflatex -interaction=nonstopmode paper.tex
	cd paper && pdflatex -interaction=nonstopmode paper.tex

clean:
	rm -f temp/clean_data.csv
	rm -f output/tables/main_result.tex
	rm -f paper/paper.pdf
	rm -f paper/paper.aux
	rm -f paper/paper.log
