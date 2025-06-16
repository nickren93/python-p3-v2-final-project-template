# lib/models/employee.py
from models.__init__ import CURSOR, CONN
from models.division import Division


class Fighter:

    # Dictionary of objects saved to the database.
    all = {}

    def __init__(self, name, record, division_id, id=None):
        self.id = id
        self.name = name
        self.record = record
        self.division_id = division_id

    def __repr__(self):
        return (
            f"<Employee {self.id}. Name: {self.name}, Record: {self.record}"
        )

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                "Name must be a non-empty string"
            )

    @property
    def record(self):
        return self._record

    @record.setter
    def record(self, record):
        if isinstance(record, str) and len(record):
            self._record = record
        else:
            raise ValueError(
                "Fighter's record must be a non-empty string"
            )

    @property
    def division_id(self):
        return self._division_id

    @division_id.setter
    def division_id(self, division_id):
        if type(division_id) is int and Division.find_by_id(division_id):
            self._division_id = division_id
        else:
            raise ValueError(
                "division_id must reference a division in the database")

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Fighter instances """
        sql = """
            CREATE TABLE IF NOT EXISTS fighters (
            id INTEGER PRIMARY KEY,
            name TEXT,
            record TEXT,
            division_id INTEGER,
            FOREIGN KEY (division_id) REFERENCES divisions(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Fighter instances """
        sql = """
            DROP TABLE IF EXISTS fighters;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name, record, and division id values of the current Fighter object.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
                INSERT INTO fighters (name, record, division_id)
                VALUES (?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, self.record, self.division_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        """Update the table row corresponding to the current Fighter instance."""
        sql = """
            UPDATE fighters
            SET name = ?, record = ?, division_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.record,
                             self.division_id, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Fighter instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM fighters
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def create(cls, name, record, division_id):
        """ Initialize a new Fighter instance and save the object to the database """
        fighter = cls(name, record, division_id)
        fighter.save()
        return fighter

    @classmethod
    def instance_from_db(cls, row):
        """Return an Fighter object having the attribute values from the table row."""

        # Check the dictionary for existing instance using the row's primary key
        fighter = cls.all.get(row[0])
        if fighter:
            # ensure attributes match row values in case local instance was modified
            fighter.name = row[1]
            fighter.record = row[2]
            fighter.division_id = row[3]
        else:
            # not in dictionary, create new instance and add to dictionary
            fighter = cls(row[1], row[2], row[3])
            fighter.id = row[0]
            cls.all[fighter.id] = fighter
        return fighter

    @classmethod
    def get_all(cls):
        """Return a list containing one Fighter object per table row"""
        sql = """
            SELECT *
            FROM fighters
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return Fighter object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM fighters
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        """Return Fighter object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM fighters
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
