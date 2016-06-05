'''
Data pre-setup for Web page
'''
import media
import fresh_tomatoes

RUN_LOLA_RUN = media.Movie(
    "Run Lola Run",
    "After a botched money delivery, Lola has 20 minutes to come up with \
    100,000 Deutschmarks",
    "http://www.impawards.com/1999/posters/run_lola_run_ver3_xlg.jpg",
    "https://www.youtube.com/watch?v=uz2-D4lY2qg",
    "1998")

AVATAR = media.Movie(
    "Avatar",
    "A marine on an alien planet",
    "http://www.impawards.com/2009/posters/avatar.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY",
    "2009")

TAKEN = media.Movie(
    "Taken",
    "A retired CIA agent relies on his old skills to save his daughter, \
    who has been kidnapped",
    "http://www.impawards.com/2009/posters/taken_ver3.jpg",
    "https://www.youtube.com/watch?v=uPJVJBm9TPA",
    "2008")

MOVIES = [RUN_LOLA_RUN, AVATAR, TAKEN]

fresh_tomatoes.open_movies_page(MOVIES)
