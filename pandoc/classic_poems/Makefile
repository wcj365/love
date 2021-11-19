# Directory with the markdown files. Defaults to "src"
SOURCEDIR ?= .
# Generate EPUB file
epub:
	pandoc --pdf-engine=xelatex -V CJKmainfont="AR PL UKai TW" config.yml \
	`find $(SOURCEDIR) -name '*.md' | sort` \
	-o $(OUTDIR)/$(PROJECT).epub


# Generate PDF file
pdf:
	pandoc --pdf-engine=xelatex  `find . -name '*.md' | sort` -o wcj365_classic.pdf
