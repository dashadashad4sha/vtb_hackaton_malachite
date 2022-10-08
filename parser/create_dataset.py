import csv

cort_text = ("human_text", "machine_text", "name", "tags", "undername", "href", "views", "comments", "for_who")


def create(c, writer):
    writer.writerow(c)
