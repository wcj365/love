# Directory with the markdown files. Defaults to "src"
SOURCEDIR ?= .
# Generate EPUB file
epub:
	pandoc --pdf-engine=xelatex -V CJKmainfont="AR PL UKai TW" config.yml \
	`find $(SOURCEDIR) -name '*.md' | sort` \
	-o $(OUTDIR)/$(PROJECT).epub


# Generate PDF file
pdf_classic:
	pandoc --pdf-engine=xelatex  `find . -name '*.md' | sort` -o wcj365_classic.pdf

# Generate PDF file
pdf_modern:
	pandoc --pdf-engine=xelatex  `find . -name '*.md' | sort` -o wcj365_modern.pdf

# Generate PDF file
pdf_proses:
	pandoc --pdf-engine=xelatex  `find . -name '*.md' | sort` -o wcj365_proses.pdf

# Generate PDF file
pdf_english:
	pandoc --pdf-engine=xelatex  `find . -name '*.md' | sort` -o wcj365_english.pdf