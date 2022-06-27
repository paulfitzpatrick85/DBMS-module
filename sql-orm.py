from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")  # point to database location, /// is hosted local in workspace
base = declarative_base()   # grab meta data froom table schema, create sub class to map everything back


# create class based modal for "Artist" table
class Artist(base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)


# create class based modal for "Album" table
class Album(base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key=True)   # primary for this table
    Name = Column(String)
    ArtistId = Column(Integer, ForeignKey("Artist.ArtistId"))  # pointing to artist table -> artist id


# create class based modal for "Track" table
class Track(base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey(Album.AlbumId))
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    Composer = Column(Integer)
    Milliseconds = Column(Integer, primary_key=False)
    Bytes = Column(Integer, primary_key=False)
    UnitPrice = Column(Float)


# instead of connecting to the datbase directly, we will ask for a session
# create a new instance of sessionmaker, thn point to our engine (the db)
Session = sessionmaker(db)

# open an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)


# Query 1 - select all records from the 'Artist' table
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.ArtistId, artist.Name, sep=" | ")  # sep is 'separated by'


#  Query 2 - select only the "Name" column from the "Artist" table
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.Name) 


# Query 3 - select only "Queen" from the "Artist" table    
# artist = session.query(Artist).filter_by(Name="Queen").first()  #  only give 1st item from query
# print(artist.ArtistId, artist.Name, sep=" | ")


# Query 4 - select only by "ArtistId" #51 from the "Artist" table
# artist = session.query(Artist).filter_by(ArtistId=51).first()  #  only give 1st item from query
# print(artist.ArtistId, artist.Name, sep=" | ")


# Query 5 - select only the albums with "ArtistId" #51 on the "Album" table
# albums = session.query(Album).filter_by(ArtistId=51)  # filtering by foreign key on line 24
# for album in albums:
#     print(album.AlbumId, album.Title, Album.ArtistId, sep=" | ")        # *********not working**************


# Query 6 - select all tracks where the composer is "Queen" from the "Track" table
tracks = session.query(Track).filter_by(Composer="Queen")
for track in tracks:
    print(
        track.TrackId,
        track.Name,
        track.AlbumId,
        track.MediaTypeId,
        track.GenreId,
        track.Composer,
        track.Milliseconds,
        track.Bytes,
        track.UnitPrice,
        sep=" | "
    )



