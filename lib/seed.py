#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.division import Division
from models.fighter import Fighter

def seed_database():
    Fighter.drop_table()
    Division.drop_table()
    Division.create_table()
    Fighter.create_table()

    # Create seed data
    lightweight = Division.create("Lightweight Division", 155)
    featherweight = Division.create("Featherweight Division", 145)
    Fighter.create("Islam Makhachev", "27-1-0 (W-L-D)", lightweight .id)
    Fighter.create("Arman Tsarukyan", "22-3-0 (W-L-D)", lightweight .id)
    Fighter.create("Charles Oliveira", "35-10-0 (W-L-D)", lightweight .id)
    Fighter.create("Ilia Topuria", "16-0-0 (W-L-D)", featherweight.id)
    Fighter.create("Alexander Volkanovski", "27-4-0 (W-L-D)", featherweight.id)
    Fighter.create("Max Holloway", "26-8-0 (W-L-D)", featherweight.id)


seed_database()
print("Seeded database")