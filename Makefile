FIND = find . -name

DELETE = xargs -I {} -0 rm -vrf "{}"

clean:
	$(FIND) "__pycache__" -print0 | $(DELETE)
	$(FIND) ".ok_*" -print0 | $(DELETE)
