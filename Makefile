t2022.tex : t2022.lyx
	lyx -e xetex t2022.lyx
	python3 tex-for-plasTeX.py
.PHONY : chirun
chirun : t2022.tex
	. ~/chirun_env/bin/activate; chirun; deactivate


