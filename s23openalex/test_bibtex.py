import pytest
from s23openalex.works import Works


def test_bibtex():
    w = Works("https://doi.org/10.1021/acscatal.5b00538")
    assert (
        w.bibtex
        == "@journal{https://openalex.org/W2288114809,\n author = {John R. Kitchin},\n doi = {https://doi.org/10.1021/acscatal.5b00538},\n journal = {ACS Catalysis},\n pages = {3894-3899},\n title = {Examples of Effective Data Sharing in Scientific Publishing},\n volume = {5},\n year = {2015}\n}\n"
    )
