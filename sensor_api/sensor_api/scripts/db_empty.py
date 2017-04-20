from sensor_api import db

# Empty each table in the database
for table in reversed(db.metadata.sorted_tables):
    db.session.delete(table)

# Commit our changes
db.session.commit()
