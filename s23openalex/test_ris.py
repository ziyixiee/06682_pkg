import pytest
from s23openalex.works import Works


def test_ris():
    w = Works("https://doi.org/10.1021/acscatal.5b00538")
    assert (
        w.ris._repr_html_()
        == '<pre>TY  - JOUR\nAU  - John R. Kitchin\nPY  - 2015\nTI  - Examples of Effective Data Sharing in Scientific Publishing\nJO  - ACS Catalysis\nVL  - 5\nIS  - 6\nSP  - 3894\nEP  - 3899\nDO  - https://doi.org/10.1021/acscatal.5b00538\nER  -<pre><br><a href="data:text/plain;base64,VFkgIC0gSk9VUgpBVSAgLSBKb2huIFIuIEtpdGNoaW4KUFkgIC0gMjAxNQpUSSAgLSBFeGFtcGxlcyBvZiBFZmZlY3RpdmUgRGF0YSBTaGFyaW5nIGluIFNjaWVudGlmaWMgUHVibGlzaGluZwpKTyAgLSBBQ1MgQ2F0YWx5c2lzClZMICAtIDUKSVMgIC0gNgpTUCAgLSAzODk0CkVQICAtIDM4OTkKRE8gIC0gaHR0cHM6Ly9kb2kub3JnLzEwLjEwMjEvYWNzY2F0YWwuNWIwMDUzOApFUiAgLQ==" download="ris">Download RIS</a>'
    )
