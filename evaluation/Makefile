
PLOT_DIR := plots
PLOT_LOG := plot.log
PALETTE_NUM=1

plots: accuracy-plots runtime-plots histogram-plots

.ONESHELL:
.SILENT:
accuracy-plots: plotdir
	export PALETTE="$$(jq --arg palette $(PALETTE_NUM) '.[$$palette]' palettes.json)"
	echo "[+] Creating accuracy fragment plots."
	python3 4-3-accuracy/plot_fragment_accuracy.py 4-3-accuracy/ssdeep_fragment.csv $(PLOT_DIR)/accuracy/real/realdata_fragments.pdf >> $(PLOT_LOG) 2>&1
	
	echo "[+] Creating synthetic plots."
	#python3 4-3-accuracy/plot_synthetic_accuracy.py 4-3-accuracy/ssdeep_comparison_synthetic.csv $(PLOT_DIR)/accuracy/synthetic/synthetic.pdf 0 >> $(PLOT_LOG) 2>&1
	

.ONESHELL:
.SILENT:
runtime-plots: plotdir
	export PALETTE="$$(jq --arg palette $(PALETTE_NUM) '.[$$palette]' palettes.json)"
	echo "[+] Creating SPHF runtime plots."
	python3 4-1-1-runtime-sphf/plot_ssdeep_runtime.py 4-1-1-runtime-sphf/ssdeep-runtime-real.csv 4-1-1-runtime-sphf/ssdeep-runtime-synthetic.csv $(PLOT_DIR)/runtime/runtime_sphf.pdf >> $(PLOT_LOG) 2>&1
	
	echo "[+] Creating CF runtime plots."
	python3 4-1-2-runtime-cf/plot_ssdeep_runtime_comparison.py 4-1-2-runtime-cf/ssdeep-runtime-comparison.csv $(PLOT_DIR)/runtime/runtime_cf_original.pdf >> $(PLOT_LOG) 2>&1
	python3 4-1-2-runtime-cf/plot_ssdeep_runtime_comparison.py 4-1-2-runtime-cf/ssdeep-runtime-comparison.csv $(PLOT_DIR)/runtime/runtime_cf_djb2.pdf >> $(PLOT_LOG) 2>&1
	
	echo "[+] Creating SPHF + CF runtime plots."
	python3 4-1-3-runtime-sphf-cf/plot_ssdeep_runtime_sphf_cf.py 4-1-3-runtime-sphf-cf/ssdeep-runtime-combined-sphf-cf.csv $(PLOT_DIR)/runtime/runtime_sphf_cf.pdf >> $(PLOT_LOG) 2>&1


.ONESHELL:
.SILENT:
histogram-plots: plotdir
	export PALETTE="$$(jq --arg palette $(PALETTE_NUM) '.[$$palette]' palettes.json)"
	echo "[+] Creating sig. length histogram."
	cd 4-2-histogram
	python3 plot_histogram.py signature-lengths.csv >> ../$(PLOT_LOG) 2>&1
	cd - > /dev/null
	mv 4-2-histogram/*.pdf $(PLOT_DIR)/hash-properties/

plotdir:
	@mkdir -p $(PLOT_DIR)/hash-properties/
	@mkdir -p $(PLOT_DIR)/runtime/
	@mkdir -p $(PLOT_DIR)/accuracy/real/
	@mkdir -p $(PLOT_DIR)/accuracy/synthetic/1000	
	@mkdir -p $(PLOT_DIR)/accuracy/synthetic/10000	
	@mkdir -p $(PLOT_DIR)/accuracy/synthetic/100000	
	@mkdir -p $(PLOT_DIR)/accuracy/synthetic/1000000	
	@mkdir -p $(PLOT_DIR)/accuracy/synthetic/10000000		


.PHONY:
clean:
	$(RM) $(PLOT_LOG)
	$(RM) -r $(PLOT_DIR)
