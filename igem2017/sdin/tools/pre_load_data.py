﻿# -*- coding: utf-8 -*-

"""
preload parts,works and circuits data into database
"""
from ..models import *
import os
import csv

# load parts data
def get_parts_type(filename):
    if "other_DNA" in filename:
        return str("other_DNA")
    elif "_" in filename:
        return "%s" % filename[0 : filename.index("_")]
    else:
        return "%s" % filename[0 : filename.index(".")]


def load_parts(parts_floder_path):
    Parts.objects.all().delete()
    for root, dirs, files in os.walk(parts_floder_path):
        for name in files:
            filepath = os.path.join(root,name)
            csv_reader = csv.reader(open(filepath, encoding='utf-8'))
            part_type = get_parts_type(name)

            row_cnt = 0
            for row in csv_reader:
                row_cnt += 1
                if (row_cnt == 1):
                    continue
                else:
                    quary = Parts.objects.filter(Name =row[0])
                    if not quary.exists():
                        try:
                            Parts.objects.create(
                                Name = row[0],
                                Description = row[1],
                                Type = row[2],
                                Subpart = row[3],
                                Safety = row[4],
                                Sequence = row[5]
                            )
                        except:
                            pass

#load works data
def load_works(works_floder_path):
    Works.objects.all().delete()
    for root, dirs, files in os.walk(works_floder_path):
        for name in files:
            filepath = os.path.join(root,name)
            csv_reader = csv.reader(open(filepath, encoding='utf-8'))

            row_cnt = 0
            for row in csv_reader:
                row_cnt += 1
                if (row_cnt > 1):
                    quary = Works.objects.filter(TeamID=row[0])
                    if not quary.exists():
                        try:
                            Works.objects.create(
                                TeamID = int(row[0]),
                                Teamname = row[1],
                                Region = row[2],
                                Country = row[3],
                                Track = row[4],
                                Section = row[5],
                                Size = int(row[6]),
                                Status = row[7],
                                Year = int(row[8]),
                                Wiki = row[9],
                                Medal = row[10],
                                Award = row[11],
                                Name = row[12],
                                Use_parts = row[13],
                            )
                        except:
                            pass


def pre_load_data(currentpath):
    parts_path = currentpath + os.sep + "parts"
    works_path = currentpath + os.sep + "works"
    load_parts(parts_path)
    load_works(works_path)
