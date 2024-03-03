import configparser


# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')

# DROP TABLES

staging_events_table_drop = "DROP TABLE staging_events"
staging_songs_table_drop = "DROP TABLE staging_songs"
songplay_table_drop = "DROP TABLE staging_songplay"
user_table_drop = "DROP TABLE user"
song_table_drop = "DROP TABLE song"
artist_table_drop = "DROP TABLE artist"
time_table_drop = "DROP TABLE time"

# CREATE TABLES
staging_events_table_create= (""" CREATE TABLE staging_events(
                            artist VARCHAR,
                            auth VARCHAR,
                            firstName VARCHAR,
                            gender VARCHAR,
                            itemInSession INTEGER,
                            lastName VARCHAR,
                            length FLOAT,
                            level INTEGER,
                            location VARCHAR,
                            method VARCHAR,
                            page VARCHAR,
                            registration FLOAT,
                            sessionId INTEGER,
                            song VARCHAR,
                            status INTEGER,
                            ts date,
                            userAgent VARCHAR,
                            userId INTEGER                            
)
""")


staging_songs_table_create = (""" CREATE TABLE staging_songs(
                            num_songs INTEGER,
                            artist_id INTEGER,
                            artist_latitude FLOAT,
                            artist_longitude FLOAT,
                            artist_location VARCHAR,
                            artist_name VARCHAR,
                            song_id VARCHAR,
                            title VARCHAR,
                            duration float,
                            year INTEGER
)
""")

songplay_table_create = ("""
""")

user_table_create = ("""
""")

song_table_create = ("""
""")

artist_table_create = ("""
""")

time_table_create = ("""
""")

# STAGING TABLES

staging_events_copy = ("""
""").format()

staging_songs_copy = ("""
""").format()

# FINAL TABLES

songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")

time_table_insert = ("""
""")

# QUERY LISTS

create_table_queries = [staging_events_table_create, staging_songs_table_create, songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [staging_events_table_drop, staging_songs_table_drop, songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]
