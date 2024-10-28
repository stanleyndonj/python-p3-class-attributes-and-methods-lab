class Song:
    # Class attributes
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
       
        # Increment song count
        Song.add_song_to_count()
       
        # Add to genre and artist lists
        Song.add_to_genres(self.genre)
        Song.add_to_artists(self.artist)
       
        # Add to genre and artist count
        Song.add_to_genre_count(self.genre)
        Song.add_to_artist_count(self.artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1


def main():
    # Create a few songs to test
    song1 = Song("99 Problems", "Jay-Z", "Rap")
    song2 = Song("Hotline Bling", "Drake", "Pop")
    song3 = Song("Formation", "Beyonce", "Pop")
    song4 = Song("Run This Town", "Jay-Z", "Rap")
    song5 = Song("Old Town Road", "Lil Nas X", "Country")

    # Output test results
    print("Total number of songs created:", Song.count)
    print("List of artists:", Song.artists)
    print("List of genres:", Song.genres)
    print("Number of songs per genre:", Song.genre_count)
    print("Number of songs per artist:", Song.artist_count)


def test_song_class():
    # Test 1: Song count
    Song.count = 0
    song1 = Song("Test Song 1", "Test Artist 1", "Test Genre 1")
    assert Song.count == 1, f"Test 1 failed: Expected 1, got {Song.count}"

    # Test 2: Artists list
    assert "Test Artist 1" in Song.artists, f"Test 2 failed: Expected 'Test Artist 1', got {Song.artists}"

    # Test 3: Genres list
    assert "Test Genre 1" in Song.genres, f"Test 3 failed: Expected 'Test Genre 1', got {Song.genres}"

    # Test 4: Genre count
    assert Song.genre_count["Test Genre 1"] == 1, f"Test 4 failed: Expected 1 for 'Test Genre 1', got {Song.genre_count}"

    # Test 5: Artist count
    assert Song.artist_count["Test Artist 1"] == 1, f"Test 5 failed: Expected 1 for 'Test Artist 1', got {Song.artist_count}"

    # Add another song to test increment behavior
    song2 = Song("Test Song 2", "Test Artist 1", "Test Genre 2")

    # Test 6: Song count increment
    assert Song.count == 2, f"Test 6 failed: Expected 2, got {Song.count}"

    # Test 7: New genre added
    assert "Test Genre 2" in Song.genres, f"Test 7 failed: Expected 'Test Genre 2', got {Song.genres}"

    # Test 8: Same artist in the artist count incremented
    assert Song.artist_count["Test Artist 1"] == 2, f"Test 8 failed: Expected 2 for 'Test Artist 1', got {Song.artist_count}"

    print("All tests passed!")


if __name__ == "__main__":
    # Run the main function to see results
    main()

    # Run tests to verify functionality
    test_song_class()